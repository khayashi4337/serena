import logging
import os
import pathlib
import subprocess

from solidlsp.ls_config import LanguageServerConfig
from solidlsp.ls_logger import LanguageServerLogger
from solidlsp.settings import SolidLSPSettings

from .clangd_language_server import ClangdLanguageServer


class MQL5Server(ClangdLanguageServer):
    """
    Provides MQL5 specific instantiation of the LanguageServer class using clangd as a backend.
    It extends ClangdLanguageServer to set up a custom environment for MQL5.
    """

    def __init__(
        self,
        config: LanguageServerConfig,
        logger: LanguageServerLogger,
        repository_root_path: str,
        solidlsp_settings: SolidLSPSettings,
    ):
        """
        Creates a MQL5Server instance.
        This class is not meant to be instantiated directly. Use LanguageServer.create() instead.
        """
        self._setup_mql5_environment(logger, repository_root_path, solidlsp_settings)

        super().__init__(config, logger, repository_root_path, solidlsp_settings)

    def _setup_mql5_environment(
        self,
        logger: LanguageServerLogger,
        repository_root_path: str,
        solidlsp_settings: SolidLSPSettings,
    ):
        """
        Clones MQL5 headers and creates compile_flags.txt for clangd.
        """
        mql5_server_resources_dir = self.ls_resources_dir(solidlsp_settings, mkdir=True)
        logger.log(f"[DEBUG] mql5_server_resources_dir: {mql5_server_resources_dir}", logging.INFO)

        mql5_headers_dir = os.path.join(mql5_server_resources_dir, "mql5_headers")
        mql5_repo_url = "https://github.com/khayashi4337/mql5.git"

        if not os.path.exists(os.path.join(mql5_headers_dir, ".git")):
            logger.log(f"Cloning MQL5 headers from {mql5_repo_url} into {mql5_headers_dir}", logging.INFO)
            try:
                subprocess.run(
                    ["git", "clone", mql5_repo_url, mql5_headers_dir],
                    check=True,
                    capture_output=True,
                    text=True,
                )
            except subprocess.CalledProcessError as e:
                logger.log(f"Failed to clone MQL5 headers repository: {e.stderr}", logging.ERROR)
                raise

        compile_flags_path = os.path.join(repository_root_path, "compile_flags.txt")
        include_path = os.path.join(mql5_headers_dir, "Include")
        include_path_posix = pathlib.Path(include_path).as_posix()
        logger.log(f"[DEBUG] include_path_posix: {include_path_posix}", logging.INFO)

        flags = f"-I{include_path_posix}\n--include=Core/MQL5.mqh\n-std=c++11\n-xc++\n-Wno-write-strings"

        # Always write the compile flags to ensure they are up to date.
        # This avoids issues with stale or incorrect configuration.
        logger.log(f"Writing compile_flags.txt at {compile_flags_path}", logging.INFO)
        with open(compile_flags_path, "w") as f:
            f.write(flags)
