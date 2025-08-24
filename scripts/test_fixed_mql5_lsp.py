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
    diagnostics_captured = {}
    diagnostics_event = threading.Event()

    def diagnostics_handler(params):
        """LSPからの診断メッセージを処理するハンドラ"""
        uri = params['uri']
        diagnostics = params['diagnostics']

        # 診断情報を更新（空でない診断のみ保存）
        if diagnostics:
            diagnostics_captured[uri] = diagnostics
        diagnostics_event.set()

    # 修正済みファイルをテスト
    with ls.start_server():
        ls.server.on_notification("textDocument/publishDiagnostics", diagnostics_handler)
        test_file_path = "mql5_test_project/ExpertAdvisor_Sample_Fixed.mq5"
        absolute_file_path = os.path.join(REPO_ROOT, test_file_path)
        file_uri = Path(absolute_file_path).as_uri()

        with ls.open_file(test_file_path):
            diagnostics_event.wait(timeout=10)

    print("\n--- Fixed File Test Results ---")
    if diagnostics_captured:
        file_uri = Path(os.path.join(REPO_ROOT, test_file_path)).as_uri()
        if file_uri in diagnostics_captured:
            print(f"Diagnostics for {test_file_path}:")
            all_diagnostics = diagnostics_captured.get(file_uri, [])
            
            if all_diagnostics:
                # セミコロンエラーがないことを確認
                semicolon_errors = [d for d in all_diagnostics if d.get('code') == 'expected_semi_declaration']
                if not semicolon_errors:
                    print("  ✅ SUCCESS: セミコロンエラーが解消されました！")
                else:
                    print("  ❌ FAILED: まだセミコロンエラーが残っています")
                
                print(f"  Found {len(all_diagnostics)} diagnostic(s):")
                for i, diag in enumerate(all_diagnostics, 1):
                    msg = diag.get('message', '').replace('\n', ' ')
                    line = diag.get('range', {}).get('start', {}).get('line', -1) + 1
                    code = diag.get('code', '')
                    severity = diag.get('severity', 1)
                    severity_text = {1: "ERROR", 2: "WARN", 3: "INFO"}.get(severity, "UNKNOWN")
                    
                    print(f"  {i}. [Line {line}] [{severity_text}] {code}")
                    print(f"     {msg}")
                    print()
            else:
                print("  ✅ PERFECT: 診断エラーが全く発生していません！")
        else:
            print(f"No diagnostics captured for {test_file_path}.")
    else:
        print(f"No diagnostics received for {test_file_path}.")

    print("\nFixed file test finished.")