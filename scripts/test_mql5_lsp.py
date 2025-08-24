import os
import time
from pathlib import Path

from solidlsp.ls import SolidLanguageServer
from solidlsp.ls_config import Language, LanguageServerConfig
from solidlsp.ls_logger import LanguageServerLogger
from solidlsp.settings import SolidLSPSettings

REPO_ROOT = Path(__file__).parent.parent.absolute()

if __name__ == "__main__":
    logger = LanguageServerLogger("mql5_test", "mql5_test.log")
    config = LanguageServerConfig(
        code_language=Language.MQL5,
        start_independent_lsp_process=True,
        trace_lsp_communication=True,  # LSP通信をログに出力してデバッグしやすくする
    )
    solidlsp_settings = SolidLSPSettings()

    # MQL5Serverインスタンスを作成
    ls = SolidLanguageServer.create(
        config=config,
        logger=logger,
        repository_root_path=str(REPO_ROOT),
        solidlsp_settings=solidlsp_settings,
    )

    diagnostics_received = {}

    # 診断メッセージを受け取るためのハンドラを定義
    def diagnostics_handler(params):
        uri = params.get("uri", "")
        diagnostics = params.get("diagnostics", [])
        print(f"Received diagnostics for {uri}: {diagnostics}")
        diagnostics_received[uri] = diagnostics

    # LSPサーバーにハンドラを登録
    ls.server.on_notification("textDocument/publishDiagnostics", diagnostics_handler)

    # サーバーを起動し、テストを実行
    with ls.start_server():
        print("MQL5 Language Server started.")
        test_file_path = "mql5_test_project/ExpertAdvisor_Sample.mq5"
        absolute_file_path = os.path.join(REPO_ROOT, test_file_path)
        file_uri = Path(absolute_file_path).as_uri()

        with ls.open_file(test_file_path):
            print(f"Opened file: {test_file_path}")
            # サーバーがファイルを処理し、診断メッセージを送ってくるのを待つ
            print("Waiting for diagnostics...")
            time.sleep(5)  # 5秒待機

    print("\n--- Test Results ---")
    if file_uri in diagnostics_received:
        print(f"Diagnostics for {test_file_path}:")
        for diag in diagnostics_received[file_uri]:
            print(f"  - {diag}")
    else:
        print(f"No diagnostics received for {test_file_path}.")

    print("\nTest finished.")
