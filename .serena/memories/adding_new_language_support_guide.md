# Serenaへの新しい言語サポートの追加

このガイドでは、Serenaに新しいプログラミング言語のサポートを追加する方法について説明します。

## 概要

新しい言語の追加には、以下の作業が含まれます：

1.  **言語サーバーの実装** - 言語固有のサーバークラスを作成します
2.  **言語の登録** - Enumや設定に言語を追加します
3.  **テストリポジトリ** - 最小限のテストプロジェクトを作成します
4.  **テストスイート** - 包括的なテストを記述します
5.  **ランタイム依存関係** - 言語サーバーの自動ダウンロードを設定します

## ステップ1：言語サーバーの実装

### 1.1 言語サービスクラスの作成

`src/solidlsp/language_servers/`に新しいファイルを作成します（例：`new_language_server.py`）。
依存関係をすべてダウンロードする言語サーバーの参照実装として`intelephense.py`を、
事前にインストールされた依存関係が必要なLSとして`gopls.py`を、
言語サーバーをPythonパッケージとして直接インストールできるため追加の依存関係が不要な`pyright_server.py`を参考にしてください。

```python
from solidlsp.ls import SolidLanguageServer
from solidlsp.ls_config import LanguageServerConfig
from solidlsp.ls_logger import LanguageServerLogger
from solidlsp.lsp_protocol_handler.server import ProcessLaunchInfo

class NewLanguageServer(SolidLanguageServer):
    """
    NewLanguageの言語サーバー実装。
    """

    def __init__(self, config: LanguageServerConfig, logger: LanguageServerLogger, repository_root_path: str):
        # 言語サーバーのコマンドを決定
        cmd = self._get_language_server_command()

        super().__init__(
            config,
            logger,
            repository_root_path,
            ProcessLaunchInfo(cmd=cmd, cwd=repository_root_path),
            "new_language",  # LSP用の言語ID
        )

    def _get_language_server_command(self) -> list[str]:
        """言語サーバーを起動するコマンドを取得します。"""
        # 例: return ["new-language-server", "--stdio"]
        pass

    @override
    def is_ignored_dirname(self, dirname: str) -> bool:
        """言語固有の無視するディレクトリを定義します。"""
        return super().is_ignored_dirname(dirname) or dirname in ["build", "dist", "target"]
```

### 1.2 言語サーバーの検出とインストール

自動インストールが必要な言語については、C#と同様のダウンロードロジックを実装します：

```python
@classmethod
def _ensure_server_installed(cls, logger: LanguageServerLogger) -> str:
    """言語サーバーがインストールされていることを確認し、パスを返します。"""
    # まずシステムのインストールを確認
    system_server = shutil.which("new-language-server")
    if system_server:
        return system_server

    # 必要に応じてダウンロードしてインストール
    server_path = cls._download_and_install_server(logger)
    return server_path

def _download_and_install_server(cls, logger: LanguageServerLogger) -> str:
    """言語サーバーをダウンロードしてインストールします。"""
    # あなたの言語サーバーに固有の実装
    pass
```

### 1.3 LSPの初期化

必要に応じて初期化メソッドをオーバーライドします：

```python
def _get_initialize_params(self) -> InitializeParams:
    """言語固有の初期化パラメータを返します。"""
    return {
        "processId": os.getpid(),
        "rootUri": PathUtils.path_to_uri(self.repository_root_path),
        "capabilities": {
            # 言語固有の機能
        }
    }

def _start_server(self):
    """カスタムハンドラで言語サーバーを起動します。"""
    # 通知ハンドラを設定
    self.server.on_notification("window/logMessage", self._handle_log_message)

    # サーバーを起動して初期化
    self.server.start()
    init_response = self.server.send.initialize(self._get_initialize_params())
    self.server.notify.initialized({})
```

## ステップ2：言語の登録

### 2.1 Language Enumへの追加

`src/solidlsp/ls_config.py`で、`Language` enumにあなたの言語を追加します：

```python
class Language(str, Enum):
    # 既存の言語...
    NEW_LANGUAGE = "new_language"

    def get_source_fn_matcher(self) -> FilenameMatcher:
        match self:
            # 既存のケース...
            case self.NEW_LANGUAGE:
                return FilenameMatcher("*.newlang", "*.nl")  # ファイル拡張子
```

### 2.2 言語サーバーファクトリの更新

`src/solidlsp/ls.py`で、`create`メソッドにあなたの言語を追加します：

```python
@classmethod
def create(cls, config: LanguageServerConfig, logger: LanguageServerLogger, repository_root_path: str) -> "SolidLanguageServer":
    match config.code_language:
        # 既存のケース...
        case Language.NEW_LANGUAGE:
            from solidlsp.language_servers.new_language_server import NewLanguageServer
            return NewLanguageServer(config, logger, repository_root_path)
```

## ステップ3：テストリポジトリ

### 3.1 テストプロジェクトの作成

`test/resources/repos/new_language/test_repo/`に最小限のプロジェクトを作成します：

```
test/resources/repos/new_language/test_repo/
├── main.newlang              # メインのソースファイル
├── lib/
│   └── helper.newlang       # テスト用の追加ソース
├── project.toml             # プロジェクト設定（該当する場合）
└── .gitignore              # ビルド成果物を無視
```

### 3.2 ソースファイルの例

以下を実証する意味のあるソースファイルを作成します：

-   **クラス/型** - シンボルテスト用
-   **関数/メソッド** - 参照検索用
-   **インポート/依存関係** - ファイル間の操作用
-   **ネストされた構造** - 階層的なシンボルテスト用

`main.newlang`の例：
```
import lib.helper

class Calculator {
    func add(a: Int, b: Int) -> Int {
        return a + b
    }

    func subtract(a: Int, b: Int) -> Int {
        return helper.subtract(a, b)  // インポートされた関数への参照
    }
}

class Program {
    func main() {
        let calc = Calculator()
        let result = calc.add(5, 3)  // addメソッドへの参照
        print(result)
    }
}
```

## ステップ4：テストスイート

### 4.1 基本テスト

`test/solidlsp/new_language/test_new_language_basic.py`を作成します。少なくとも以下をテストする必要があります：

1.  シンボルの検索
2.  ファイル内参照の検索
3.  ファイル間参照の検索

テストすべき内容の例として`test/solidlsp/php/test_php_basic.py`を参照してください。
`pytest.ini`に新しい言語マーカーを追加することを忘れないでください。

### 4.2 統合テスト

`test_serena_agent.py`のパラメーター化されたテストに、新しい言語のケースを追加することを検討してください。

### 5. ドキュメント

以下を更新してください：

-   **README.md** - サポートされている言語リストに言語を追加
-   **CHANGELOG.md** - 新しい言語サポートを文書化
-   **言語固有のドキュメント** - インストール要件、既知の問題
