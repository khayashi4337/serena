import os
import time
import logging
import threading
from pathlib import Path

from src.solidlsp.ls import SolidLanguageServer
from src.solidlsp.ls_config import Language, LanguageServerConfig
from src.solidlsp.ls_logger import LanguageServerLogger
from src.solidlsp.settings import SolidLSPSettings

REPO_ROOT = Path(__file__).parent.parent.absolute()

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger()

    # LSPサーバーのインスタンスを作成
    config = LanguageServerConfig(code_language=Language.MQL5)
    ls_logger = LanguageServerLogger(logger)
    solidlsp_settings = SolidLSPSettings()
    ls = SolidLanguageServer.create(config, ls_logger, str(REPO_ROOT), solidlsp_settings=solidlsp_settings)

    # 診断メッセージを格納するための辞書
    diagnostics_captured = {}  # 最初の空でない診断をキャプチャするための辞書
    diagnostics_event = threading.Event()

    def diagnostics_handler(params):
        """LSPからの診断メッセージを処理するハンドラ"""
        uri = params['uri']
        diagnostics = params['diagnostics']

        # 診断情報を更新（空でない診断のみ保存）
        if diagnostics:
            diagnostics_captured[uri] = diagnostics
        diagnostics_event.set()  # イベントをセットして待機を解除

    # サーバーを起動し、テストを実行
    with ls.start_server():
        # サーバー開始後に通知ハンドラーを登録
        ls.server.on_notification("textDocument/publishDiagnostics", diagnostics_handler)
        test_file_path = "mql5_test_project/ExpertAdvisor_Sample.mq5"
        absolute_file_path = os.path.join(REPO_ROOT, test_file_path)
        file_uri = Path(absolute_file_path).as_uri()

        with ls.open_file(test_file_path):
            # サーバーがファイルを処理し、診断メッセージを送ってくるのを待つ
            diagnostics_event.wait(timeout=10)

    print("\n--- Test Results ---")
    if diagnostics_captured:
        file_uri = Path(os.path.join(REPO_ROOT, test_file_path)).as_uri()
        if file_uri in diagnostics_captured:
            print(f"Diagnostics for {test_file_path}:")
            valid_errors = []
            for diag in diagnostics_captured.get(file_uri, []):
                # MQL5として有効なエラーのみフィルタリング
                msg = diag.get('message', '')
                # MQL5として重要なエラーをフィルタリング
                if ('Cannot initialize a variable of type' in msg or 
                    'error' in msg.lower() and 'template' not in msg.lower()):
                    valid_errors.append(diag)
            
            if valid_errors:
                for diag in valid_errors:
                    msg = diag.get('message', '').replace('\n', ' ')
                    line = diag.get('range', {}).get('start', {}).get('line', -1) + 1
                    print(f"  - [L:{line}] {msg}")
            else:
                print("  No significant errors found.")
        else:
            print(f"No diagnostics captured for {test_file_path}.")
    else:
        print(f"No diagnostics received for {test_file_path}.")

    print("\nTest finished.")
