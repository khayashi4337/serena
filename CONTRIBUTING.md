# Serenaへの貢献

Serenaは活発に開発が進められています。私たちは、このツールで何ができるのか、そしてどこに限界があるのかをまだ探っていく段階です。

新しいIssueの作成、機能リクエスト、拡張機能の提案などを通じて、皆さんの学びをぜひ共有してください。

## 開発環境のセットアップ

開発環境は、`uv`を使用したローカルセットアップ、またはDockerベースのセットアップが可能です。
また、このリポジトリはGitHub Codespace上でもシームレスに動作するように設定されています。以下に、それぞれのセットアップシナリオの手順を示します。

どの方法でセットアップした場合でも、`uv`を介して仮想環境を作成・有効化でき（下記参照）、フォーマット、テスト、ドキュメント構築などの様々なタスクは`poe`を使って実行できます。例えば、`poe format`を実行すると、ノートブックを含むコード全体がフォーマットされます。利用可能なコマンド一覧は`poe`とだけ実行して確認してください。

### Python (`uv`) でのセットアップ

以下の手順で、必要なパッケージを含む仮想環境をインストールできます。

1.  新しい仮想環境を作成します: `uv venv`
2.  環境を有効化します:
    *   Linux/Unix/macOS または WindowsのGit Bashの場合: `source .venv/bin/activate`
    *   上記以外のWindows環境の場合: `.venv\Scripts\activate.bat` (cmd/ps) または `source .venv/Scripts/activate` (git-bash)
3.  すべての追加機能を含む必要なパッケージをインストールします: `uv pip install -e .[all]`

    **Windowsでの注意**: 上記コマンドの実行中に `Permission denied` のような権限エラーが発生した場合、代わりに以下のコマンドをお試しください。これにより、ユーザー個別の領域にパッケージがインストールされます。

    ```shell
    pip install -e .[all] --user
    ```

## ツールのローカル実行

Serenaのツール（実際にはSerenaの全コード）は、LLMなしで実行できます。また、MCP固有の機能も不要です（ただし、必要であればmcpインスペクターを使用することも可能です）。

ツールを実行するためのサンプルスクリプトが [scripts/demo_run_tools.py](scripts/demo_run_tools.py) にあります。

## 新しい対応言語の追加

対応する[メモリ](.serena/memories/adding_new_language_support_guide.md)を参照してください。