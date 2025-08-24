<p align="center" style="text-align:center">
  <img src="resources/serena-logo.svg#gh-light-mode-only" style="width:500px">
  <img src="resources/serena-logo-dark-mode.svg#gh-dark-mode-only" style="width:500px">
</p>

* :rocket: Serenaは、LLMを**あなたのコードベースで直接**動作するフル機能のエージェントに変えることができる、強力な**コーディングエージェントツールキット**です。
  他のほとんどのツールとは異なり、特定のLLM、フレームワーク、インターフェースに縛られていないため、さまざまな方法で簡単に使用できます。
* :wrench: Serenaは、IDEの機能に似た、不可欠な**セマンティックコード検索・編集ツール**を提供します。シンボルレベルでコードエンティティを抽出し、関係構造を活用します。既存のコーディングエージェントと組み合わせることで、これらのツールは（トークン）効率を大幅に向上させます。
* :free: Serenaは**無料でオープンソース**であり、すでにお持ちのLLMの機能を無料で強化します。

SerenaはコーディングエージェントのためのIDEと考えることができます。これを使えば、エージェントはファイル全体を読んだり、grepのような検索や文字列置換を行って適切なコードを見つけて編集したりする必要がなくなります。代わりに、`find_symbol`、`find_referencing_symbols`、`insert_after_symbol`のようなコード中心のツールを使用できます。

### ユーザーからのフィードバック

ほとんどのユーザーは、非常に高性能なエージェント（Claude Codeなど）内で使用した場合でも、Serenaがコーディングエージェントの結果に強力なプラスの効果をもたらすと報告しています。Serenaはしばしば[ゲームチェンジャー](https://www.reddit.com/r/ClaudeAI/comments/1lfsdll/try_out_serena_mcp_thank_me_later/)、または絶大な[生産性向上](https://www.reddit.com/r/ClaudeCode/comments/1mguoia/absolutely_insane_improvement_of_claude_code)をもたらすものとして説明されています。

しかし、非常に小規模なプロジェクトや、1つのファイルのみが関わるタスク（ファイルのサブセットのみを読み書きする必要がないタスク）では、Serenaを含めることによるメリットは得られないかもしれません。例えば、ゼロからコードを作成する場合、Serenaはあまり価値を提供しません。
また、豊富な設定オプションを使用して、Serenaを自分のニーズやワークフローに合わせて調整することもできます。

これまでにSerenaについていくつかのビデオやブログ記事が書かれています：

#### YouTubeにて

* [AI Labs](https://www.youtube.com/watch?v=wYWyJNs1HVk&t=1s)
* [Yo Van Eyck](https://www.youtube.com/watch?v=UqfxuQKuMo8&t=45s)
* [JeredBlu](https://www.youtube.com/watch?v=fzPnM3ySmjE&t=32s)

#### ブログにて

* [Serena's Design Principles](https://medium.com/@souradip1000/deconstructing-serenas-mcp-powered-semantic-code-understanding-architecture-75802515d116)
* [Serena with Claude Code (日本語)](https://blog.lai.so/serena/)
* [Turning Claude Code into a Development Powerhouse](https://robertmarshall.dev/blog/turning-claude-code-into-a-development-powerhouse/)

### デモンストレーション1 - Claude Codeでの効率的な操作

Claude Code内でSerenaが効率的にコードを取得・編集し、トークンと時間を節約するデモンストレーションです。効率的な操作はコスト削減に役立つだけでなく、生成されるコードの品質を全体的に向上させます。この効果は非常に小規模なプロジェクトではあまり顕著ではないかもしれませんが、大規模なプロジェクトではしばしば非常に重要になります。

https://github.com/user-attachments/assets/ab78ebe0-f77d-43cc-879a-cc399efefd87

### デモンストレーション2 - Claude DesktopでのSerena

Claude Desktopを使用して、Serenaが自身のために小さな機能（より良いログGUI）を実装するデモンストレーションです。
SerenaのツールがClaudeに適切なシンボルを見つけて編集させる様子に注目してください。

https://github.com/user-attachments/assets/6eaa9aa1-610d-4723-a2d6-bf1e487ba753

<p align="center">
  <em>Serenaは活発に開発中です！最新のアップデート、今後の機能、学んだ教訓を見て、最新情報を入手してください。</em>
</p>

<p align="center">
  <a href="CHANGELOG.md">
    <img src="https://img.shields.io/badge/Updates-1e293b?style=flat&logo=rss&logoColor=white&labelColor=1e293b" alt="Changelog" />
  </a>
  <a href="roadmap.md">
    <img src="https://img.shields.io/badge/Roadmap-14532d?style=flat&logo=target&logoColor=white&labelColor=14532d" alt="Roadmap" />
  </a>
  <a href="lessons_learned.md">
    <img src="https://img.shields.io/badge/Lessons-Learned-7c4700?style=flat&logo=readthedocs&logoColor=white&labelColor=7c4700" alt="Lessons Learned" />
  </a>
</p>

### LLMインテグレーション

Serenaはコーディングワークフローに必要な[ツール](#list-of-tools)を提供しますが、実際の作業を行い、ツールの使用を調整するにはLLMが必要です。

例えば、[一行のシェルコマンド](#claude-code)で**Claude Codeのパフォーマンスを大幅に向上**させることができます。

Serenaはいくつかの方法でLLMと統合できます：

* **モデルコンテキストプロトコル（MCP）**を使用する。
   SerenaはMCPサーバーを提供し、以下と統合します。
  * Claude CodeおよびClaude Desktop、
  * Codex、Gemini-CLI、Qwen3-Coder、rovodev、OpenHands CLIなどのターミナルベースのクライアント、
  * VSCode、Cursor、IntelliJなどのIDE、
  * ClineやRoo Codeなどの拡張機能
  * [OpenWebUI](https://docs.openwebui.com/openapi-servers/mcp)、[Jan](https://jan.ai/docs/mcp-examples/browser/browserbase#enable-mcp)、[Agno](https://docs.agno.com/introduction/playground)などのローカルクライアント
* [mcpoを使用してChatGPTに接続する](docs/serena_on_chatgpt.md)か、MCPをサポートしていないがツール呼び出しをサポートしている他のクライアントに接続する。
* [こちら](docs/custom_agent.md)で示すように、Serenaのツールを任意のージェントフレームワークに組み込む。
   Serenaのツール実装はフレームワーク固有のコードから分離されているため、どのエージェントフレームワークにも簡単に適応できます。

### プログラミング言語のサポートとセマンティック分析機能

Serenaのセマンティックコード分析機能は、広く実装されている**言語サーバー**に基づいています。
言語サーバープロトコル（LSP）を使用しています。LSPは、コードのシンボリックな理解に基づいた、多機能なコードクエリ
および編集機能のセットを提供します。
これらの機能を備えたSerenaは、熟練した開発者がIDEの機能を活用するのと同じように、コードを発見し編集します。
Serenaは、非常に大規模で複雑なプロジェクトでも、適切なコンテキストを効率的に見つけ、正しいことを行うことができます！
そのため、無料でオープンソースであるだけでなく、プレミアム料金を請求する既存のソリューションよりも優れた結果を頻繁に達成します。

言語サーバーは、幅広いプログラミング言語をサポートしています。
Serenaでは、以下を提供します：

* 直接、すぐに使えるサポート：
  * Python
  * TypeScript/Javascript
  * PHP（Intelephense LSPを使用。プレミアム機能には`INTELEPHENSE_LICENSE_KEY`環境変数を設定）
  * Go（goplsのインストールが必要）
  * Rust（[rustup](https://rustup.rs/)が必要 - ツールチェーンのrust-analyzerを使用）
  * C#
  * Ruby
  * Swift
  * Java（_注意_：起動が遅く、特に初回起動は遅いです。macOSおよびLinuxのJavaで問題が発生する可能性があり、現在対応中です。）
  * Elixir（NextLSとElixirのインストールが必要。**Windowsは非対応**）
  * Clojure
  * Bash
  * C/C++（参照の検索で問題が発生する可能性があり、現在対応中です）
  * Zig（ZLS - Zig Language Serverのインストールが必要）
  * Lua（インストールされていない場合、lua-language-serverを自動的にダウンロード）
  * Nix（nixdのインストールが必要）
  * Dart
  * MQL5（clangdを利用。C/C++に類似）
* 間接的なサポート（コードの変更/手動インストールが必要な場合があります）：
  * Kotlin（未テスト）

   これらの言語は言語サーバーライブラリでサポートされていますが、
   これらの言語のサポートが実際に完璧に機能するかどうかは明示的にテストしていません。

さらに、新しい言語サーバー実装用の浅いアダプターを提供することで、原則として他の言語も簡単にサポートできます。

## 目次

<!-- Created with markdown-toc -i README.md -->
<!-- Install it with npm install -g markdown-toc -->

<!-- toc -->

- [目次](#目次)
- [クイックスタート](#クイックスタート)
  - [Serena MCPサーバーの実行](#serena-mcpサーバーの実行)
    - [使用方法](#使用方法)
      - [uvxの使用](#uvxの使用)
        - [ローカルインストール](#ローカルインストール)
      - [Dockerの使用（実験的）](#dockerの使用実験的)
    - [SSEモード](#sseモード)
    - [コマンドライン引数](#コマンドライン引数)
  - [設定](#設定)
  - [プロジェクトのアクティベーションとインデックス作成](#プロジェクトのアクティベーションとインデックス作成)
  - [Claude Code](#claude-code)
  - [Codex](#codex)
  - [その他のターミナルベースのクライアント](#その他のターミナルベースのクライアント)
  - [Claude Desktop](#claude-desktop)
  - [MCPコーディングクライアント（Cline、Roo-Code、Cursor、Windsurfなど）](#mcpコーディングクライアントclineroo-codecursorwindsurfなど)
  - [ローカルGUIとフレームワーク](#ローカルguiとフレームワーク)
- [詳細な使用方法と推奨事項](#詳細な使用方法と推奨事項)
  - [ツールの実行](#ツールの実行)
    - [シェル実行と編集ツール](#シェル実行と編集ツール)
  - [モードとコンテキスト](#モードとコンテキスト)
    - [コンテキスト](#コンテキスト)
    - [モード](#モード)
    - [カスタマイズ](#カスタマイズ)
  - [オンボーディングとメモリ](#オンボーディングとメモリ)
  - [プロジェクトの準備](#プロジェクトの準備)
    - [コードベースの構造化](#コードベースの構造化)
    - [クリーンな状態から始める](#クリーンな状態から始める)

<!-- tocstop -->

## クイックスタート

Serenaはさまざまな方法で使用できます。以下に、いくつかの統合方法についての説明を示します。

* Claudeでのコーディングには、[Claude Code](#claude-code)または[Claude Desktop](#claude-desktop)を介してSerenaを使用することをお勧めします。また、他のほとんどの[ターミナルベースのクライアント](#その他のターミナルベースのクライアント)でもSerenaを使用できます。
* IDE外でGUIを使いたい場合は、MCPサーバーをサポートする多くの[ローカルGUI](#ローカルguiとフレームワーク)のいずれかを使用できます。
  また、[mcpo](docs/serena_on_chatgpt.md)を使用して、Serenaを多くのWebクライアント（ChatGPTを含む）に接続することもできます。
* IDEに統合されたSerenaを使用したい場合は、[他のMCPクライアント](#mcpコーディングクライアントcline-roo-code-cursor-windsurfなど)のセクションを参照してください。
* Serenaを独自のアプリケーションを構築するためのライブラリとして使用できます。公開APIは安定させようと努めていますが、それでも
  破壊的変更が予想されるため、依存関係として使用する場合はSerenaを固定バージョンにピン留めする必要があります。

Serenaは`uv`によって管理されているため、[インストール](https://docs.astral.sh/uv/getting-started/installation/)が必要です。

### Serena MCPサーバーの実行

MCPサーバーを実行するにはいくつかのオプションがあり、以下のサブセクションで説明します。

#### 使用方法

典型的な使用法では、クライアント（Claude Code、Claude Desktopなど）が
MCPサーバーをサブプロセスとして実行します（stdio通信を使用）。
そのため、クライアントにはMCPサーバーを実行するコマンドを提供する必要があります。
（または、MCPサーバーをSSEモードで実行し、クライアントに
接続方法を伝えることもできます。）

MCPサーバーをどのように実行するかにかかわらず、Serenaはデフォルトで、ログを表示し、シャットダウンを許可する小さなWebベースのダッシュボードをlocalhostで起動します。
MCPサーバー（多くのクライアントがプロセスのクリーンアップに失敗するため）。
これやその他の設定は、[設定](#設定)および/または[コマンドライン引数](#コマンドライン引数)を提供することで調整できます。

##### uvxの使用

`uvx`を使用すると、明示的なローカルインストールなしで、リポジトリから直接最新バージョンのSerenaを実行できます。

```shell
uvx --from git+https://github.com/oraios/serena serena start-mcp-server
```

CLIを調べて、serenaが提供するカスタマイズオプションのいくつかを確認してください（詳細は後述）。

###### ローカルインストール

1. リポジトリをクローンし、そのディレクトリに移動します。

   ```shell
   git clone https://github.com/oraios/serena
   cd serena
   ```

2. オプションで、ホームディレクトリの設定ファイルを編集します。

   ```shell
   uv run serena config edit
   ```

   デフォルト設定でよければ、この部分はスキップできます。Serenaを初めて実行したときに設定ファイルが作成されます。
3. `uv`でサーバーを実行します：

   ```shell
   uv run serena start-mcp-server
   ```

   serenaのインストールディレクトリ外から実行する場合は、必ずパスを渡してください。つまり、以下を使用します。

   ```shell
    uv run --directory /abs/path/to/serena serena start-mcp-server
   ```

##### Dockerの使用（実験的）

⚠️ 現在、Dockerのサポートは実験的であり、いくつかの制限があります。使用する前に、[Dockerドキュメント](DOCKER.md)で重要な注意点をお読みください。

作業したいプロジェクトがすべて`/path/to/your/projects`にあると仮定して、次のようにdocker経由でSerena MCPサーバーを直接実行できます。

```shell
docker run --rm -i --network host -v /path/to/your/projects:/workspaces/projects ghcr.io/oraios/serena:latest serena start-mcp-server --transport stdio
```

`/path/to/your/projects`をプロジェクトディレクトリへの絶対パスに置き換えてください。Dockerアプローチには次の利点があります：

* シェルコマンド実行のセキュリティ分離の向上
* 言語サーバーと依存関係をローカルにインストールする必要がない
* 異なるシステム間での一貫した環境

または、リポジトリで提供されている`compose.yml`ファイルを使用してdocker composeを使用します。

詳細なセットアップ手順、設定オプション、既知の制限については、[Dockerドキュメント](DOCKER.md)を参照してください。

#### SSEモード

ℹ️ プロトコルとしてstdioを使用するMCPサーバーは、クライアント/サーバーアーキテクチャとしてはやや珍しいことに注意してください。サーバーの標準入出力ストリームを介して通信が行われるためには、サーバーがクライアントによって起動される必要があるためです。
言い換えれば、サーバーを自分で起動する必要はありません。クライアントアプリケーション（例：Claude Desktop）がこれを処理するため、起動コマンドで設定する必要があります。

代わりにHTTPベースの通信を使用するSSEモードを使用する場合、サーバーのライフサイクルを自分で制御します。
つまり、サーバーを起動し、クライアントに接続先のURLを提供します。

`start-mcp-server`に`--transport sse`オプションを指定し、オプションでポートを指定するだけです。
たとえば、ローカルインストールを使用してSerena MCPサーバーをポート9121でSSEモードで実行するには、
Serenaディレクトリから次のコマンドを実行します。

```shell
uv run serena start-mcp-server --transport sse --port 9121
```

そして、クライアントを`http://localhost:9121/sse`に接続するように設定します。

#### コマンドライン引数

Serena MCPサーバーは、SSEモードで実行するオプションや、Serenaをさまざまな[コンテキストと操作モード](#モードとコンテキスト)に適応させるオプションなど、幅広い追加のコマンドラインオプションをサポートしています。

`--help`パラメータを付けて実行すると、利用可能なオプションのリストが表示されます。

### 設定

Serenaは設定の点で非常に柔軟です。ほとんどのユーザーにとってはデフォルト設定で十分ですが、
いくつかのyamlファイルを編集することで、ニーズに合わせて完全に調整できます。ツールを無効にしたり、Serenaの指示
（`system_prompt`と呼ぶもの）を変更したり、プロンプトのみを提供するツールの出力を調整したり、ツール記述を調整したりすることもできます。

Serenaは4つの場所で設定されます：

1. すべてのクライアントとプロジェクトに適用される一般設定用の`serena_config.yml`。
   これは、ユーザーディレクトリの`.serena/serena_config.yml`にあります。
   ファイルを明示的に作成しない場合、Serenaを初めて実行したときに自動生成されます。
   直接編集するか、以下を使用できます。

   ```shell
   uvx --from git+https://github.com/oraios/serena serena config edit
   ```

   （または`--directory`コマンドバージョンを使用します）。
2. クライアントの設定で`start-mcp-server`に渡される引数（下記参照）。
   これは、それぞれのクライアントによって開始されるすべてのセッションに適用されます。特に、[context](#contexts)パラメータは、Serenaがクライアントの既存のツールや機能に最適に調整されるように適切に設定する必要があります。
   詳細な説明については、参照してください。`serena_config.yml`のすべてのエントリは、コマンドライン引数で上書きできます。
3. プロジェクト内の`.serena/project.yml`ファイル。これは、そのプロジェクトがアクティブ化されるたびに使用されるプロジェクトレベルの設定を保持します。
   このファイルは、そのプロジェクトでSerenaを初めて使用したときに自動生成されますが、
   明示的に生成することもできます。

   ```shell
   uvx --from git+https://github.com/oraios/serena serena project generate-yml
   ```

   （または`--directory`コマンドバージョンを使用します）。
4. コンテキストとモードを介して。詳細については、[モードとコンテキスト](#モードとコンテキスト)のセクションを参照してください。

初期設定後、Serenaをどのように使用したいかに応じて、以下のセクションのいずれかに進んでください。

### プロジェクトのアクティベーションとインデックス作成

主に同じプロジェクトで作業していて、クライアントのMCP設定で`start-mcp-server`コマンドに`--project <path_or_name>`を渡すことで、起動時に常にアクティブ化するように設定できます。
これは、Claude CodeのようにMCPサーバーをプロジェクトごとに設定するクライアントに特に便利です。

それ以外の場合、推奨される方法は、LLMに絶対パスを提供するか、
過去にプロジェクトがアクティブ化された場合はその名前でプロジェクトをアクティブ化するように依頼することです。デフォルトのプロジェクト名はディレクトリ名です。

* "プロジェクト/path/to/my_projectをアクティブ化して"
* "プロジェクトmy_projectをアクティブ化して"

アクティブ化されたすべてのプロジェクトは自動的に`serena_config.yml`に追加され、各
プロジェクトに対して`.serena/project.yml`ファイルが生成されます。後者を調整できます。たとえば、名前
（アクティベーション中に参照するもの）やその他のオプションを変更できます。同じ名前の異なるプロジェクトがないことを確認してください。

ℹ️ 大規模なプロジェクトの場合、Serenaのツールを高速化するためにプロジェクトをインデックス化することをお勧めします。そうしないと、最初の
ツールの適用が非常に遅くなる可能性があります。
これを行うには、プロジェクトディレクトリからこれを実行します（またはプロジェクトへのパスを引数として渡します）：

```shell
uvx --from git+https://github.com/oraios/serena serena project index
```

（または`--directory`コマンドバージョンを使用します）。

### Claude Code

Serenaは、Claude Codeをより安価で強力にするための素晴らしい方法です！

プロジェクトディレクトリから、次のようなコマンドでserenaを追加します。

```shell
claude mcp add serena -- <serena-mcp-server> --context ide-assistant --project $(pwd)
```

ここで`<serena-mcp-server>`は、[Serena MCPサーバーを実行する方法](#running-the-serena-mcp-server)です。
たとえば、`uvx`を使用する場合、次のように実行します。

```shell
claude mcp add serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project $(pwd)
```

ℹ️ Serenaには指示テキストが付属しており、ClaudeがSerenaのツールを適切に使用するにはそれを読む必要があります。
  バージョン`v1.0.52`以降、claude codeはMCPサーバーの指示を読むため、これは**自動的に処理されます**。
  古いバージョンを使用していて、またはClaudeが指示を読み取れない場合は、明示的に
  「Serenaの初期指示を読んで」と依頼するか、`/mcp__serena__initial_instructions`を実行して指示テキストを読み込むことができます。
  これを利用したい場合は、設定の`included_optional_tools`に`initial_instructions`を追加して、対応するツールを明示的に有効にする必要があります。
  新しい会話を開始したときや、圧縮操作の後に、ClaudeがSerenaのツールを適切に使用するように設定されていることを確認するために、Claudeに指示を読ませる必要がある場合があることに注意してください。

### Codex

SerenaはOpenAIのCodex CLIとすぐに連携して動作しますが、正しく動作させるためには`codex`コンテキストを使用する必要があります。（技術的な理由は、CodexがMCP仕様を完全にサポートしていないため、ツールの調整が必要だからです。）

Claude Codeとは異なり、CodexではMCPサーバーをプロジェクトごとではなくグローバルに追加します。以下を
`~/.codex/config.toml`に追加します（ファイルが存在しない場合は作成します）：

```toml
[mcp_servers.serena]
command = "uvx"
args = ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "codex"]
```

Codexが起動したら、プロジェクトをアクティブ化する必要があります。これは次のように言うことで実行できます：

"serenaを使用して現在のディレクトリをプロジェクトとしてアクティブ化する"

> プロジェクトをアクティブ化しないと、Serenaのツールを使用できません！

以上です！ `~/.codex/log/codex-tui.log`を見て、エラーが発生していないか確認してください。

設定で無効にしていない場合、Serenaダッシュボードは実行されますが、Codexのサンドボックス化のため、Webブラウザが
自動的に開かない場合があります。`http://localhost:24282/dashboard/index.html`（または
そのポートがすでに使用されている場合はより高いポート）に手動でアクセスして開くことができます。

> Codexは、ツールが正常に実行された場合でも、しばしば`failed`と表示します。これは問題ではなく、Codexのバグのようです。エラーメッセージにもかかわらず、すべてが期待どおりに機能します。

### その他のターミナルベースのクライアント

[Codex](https://github.com/openai/codex?tab=readme-ov-file#model-context-protocol-mcp)、
[Gemini-CLI](https://github.com/google-gemini/gemini-cli)、[Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder)、
[rovodev](https://community.atlassian.com/forums/Rovo-for-Software-Teams-Beta/Introducing-Rovo-Dev-CLI-AI-Powered-Development-in-your-terminal/ba-p/3043623)、
[OpenHands CLI](https://docs.all-hands.dev/usage/how-to/cli-mode)、[opencode](https://github.com/sst/opencode)など、MCPサーバーをサポートする多くのターミナルベースのコーディングアシスタントがあります。

これらは一般的に、Serenaが提供するシンボリックツールの恩恵を受けます。独自のコンテキスト、モード、またはプロンプトを作成して、ワークフロー、使用している他のMCPサーバー、およびクライアントの内部機能に合わせてSerenaのいくつかの側面をカスタマイズしたい場合があります。

### Claude Desktop

[Claude Desktop](https://claude.ai/download)（WindowsおよびmacOSで利用可能）の場合、[ファイル] / [設定] / [開発者] / [MCPサーバー] / [設定の編集]に移動し、
JSONファイル`claude_desktop_config.json`を開きます。
セットアップに応じて[実行コマンド](#running-the-serena-mcp-server)を使用して、`serena` MCPサーバー設定を追加します。

* ローカルインストール：

   ```json
   {
       "mcpServers": {
           "serena": {
               "command": "/abs/path/to/uv",
               "args": ["run", "--directory", "/abs/path/to/serena", "serena", "start-mcp-server"]
           }
       }
   }
   ```

* uvx:

   ```json
   {
       "mcpServers": {
           "serena": {
               "command": "/abs/path/to/uvx",
               "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server"]
           }
       }
  }
  ```

* docker:

  ```json
   {
       "mcpServers": {
           "serena": {
               "command": "docker",
               "args": ["run", "--rm", "-i", "--network", "host", "-v", "/path/to/your/projects:/workspaces/projects", "ghcr.io/oraios/serena:latest", "serena", "start-mcp-server", "--transport", "stdio"]
           }
       }
   }
   ```

Windowsでパスにバックスラッシュを含むパスを使用する場合
（フォワードスラッシュも使用できることに注意してください）、正しくエスケープしてください（`\\`）。

以上です！設定を保存し、Claude Desktopを再起動します。最初のプロジェクトをアクティブ化する準備ができました。

ℹ️ 追加の引数を使用して実行コマンドをさらにカスタマイズできます（[上記](#command-line-arguments)参照）。

注意：WindowsとmacOSにはAnthropicによる公式のClaude Desktopアプリケーションがありますが、Linuxには[オープンソースの
コミュニティバージョン](https://github.com/aaddrick/claude-desktop-debian)があります。

⚠️ Claudeを閉じるとシステムトレイに最小化されるだけなので、Claude Desktopアプリケーションを完全に終了するようにしてください（少なくともWindowsでは）。

⚠️ 一部のクライアントはゾンビプロセスを残す可能性があります。その場合は手動で見つけて終了させる必要があります。
    Serenaでは、[ダッシュボード](#serenas-logs-the-dashboard-and-gui-tool)をアクティブにして、気づかれないプロセスを防ぎ、ダッシュボードを
    Serenaのシャットダウンに使用することもできます。

再起動後、チャットインターフェイスにSerenaのツールが表示されるはずです（小さなハンマーアイコンに注目してください）。

Claude DesktopでのMCPサーバーの詳細については、[公式クイックスタートガイド](https://modelcontextprotocol.io/quickstart/user)を参照してください。

### MCPコーディングクライアント（Cline、Roo-Code、Cursor、Windsurfなど）

MCPサーバーであるため、SerenaはどのMCPクライアントにも含めることができます。上記と同じ設定で、
おそらくクライアント固有の小さな変更を加えるだけで、動作するはずです。人気の
既存のコーディングアシスタント（IDE拡張機能またはVSCodeライクなIDE）のほとんどは、MCPサーバーへの接続をサポートしています。
これらの統合には**`ide-assistant`コンテキストを使用することをお勧めします**。MCPクライアントの設定の`args`に`"--context", "ide-assistant"`を追加します。Serenaを含めると、シンボリック操作のためのツールが提供されるため、一般的にパフォーマンスが向上します。

この場合、使用料金の請求は、選択したクライアントによって引き続き管理されます
（Claude Desktopクライアントとは異なります）。しかし、次のような理由で、このようなアプローチでSerenaを使用したい場合があるかもしれません。

1. すでにコーディングアシスタント（ClineやCursorなど）を使用していて、それをより強力にしたいだけの場合。
2. Linuxを使用していて、[コミュニティ作成のClaude Desktop](https://github.com/aaddrick/claude-desktop-debian)を使用したくない場合。
3. SerenaをIDEに緊密に統合したいが、そのための支払いを厭わない場合。

### ローカルGUIとフレームワーク

ここ数ヶ月で、強力なローカルGUIを実行し、それをMCPサーバーに接続できるいくつかのテクノロジーが登場しました。
これらはSerenaとすぐに連携して動作します。これを可能にする主要なオープンソースGUIテクノロジーには、
[Jan](https://jan.ai/docs/mcp)、[OpenHands](https://github.com/All-Hands-AI/OpenHands/)、
[OpenWebUI](https://docs.openwebui.com/openapi-servers/mcp)、[Agno](https://docs.agno.com/introduction/playground)があります。
これらにより、SerenaをほぼすべてのLLM（ローカルで実行されているものを含む）と組み合わせることができ、さまざまな他の統合も提供されます。

## 詳細な使用方法と推奨事項

### ツールの実行

Serenaは、セマンティックコード検索ツールと編集機能、シェル実行を組み合わせています。
Serenaの動作は、[モードとコンテキスト](#モードとコンテキスト)を通じてさらにカスタマイズできます。
ツールの完全なリストは[以下](#full-list-of-tools)にあります。

すべてのツールの使用が一般的に推奨されます。これにより、Serenaが最大の価値を提供できるようになります。
シェルコマンド（特にテスト）を実行することによってのみ、Serenaは自律的に間違いを特定し修正できます。

#### シェル実行と編集ツール

ただし、`execute_shell_command`ツールは任意のコード実行を許可することに注意してください。
SerenaをMCPサーバーとして使用する場合、クライアントは通常、ツールを実行する前にユーザーに許可を求めます。
そのため、ユーザーが実行パラメータを事前に検査する限り、これは問題にはなりません。
ただし、懸念がある場合は、プロジェクトの.yml設定ファイルで特定のコマンドを無効にすることを選択できます。
コードベースを変更せずに、純粋にコードを分析して実装を提案するためにSerenaを使用したい場合は、プロジェクト設定ファイルで`read_only: true`を設定して読み取り専用モードを有効にできます。
これにより、すべての編集ツールが自動的に無効になり、コードベースへの変更が防止されますが、
すべての分析および探索機能は引き続き使用できます。

一般的に、作業内容をバックアップし、バージョン管理システムを使用して、
作業内容が失われないようにしてください。

### モードとコンテキスト

Serenaの動作とツールセットは、コンテキストとモードを使用して調整できます。
これらにより、ワークフローとSerenaが動作する環境に最適に適合するように、高度なカスタマイズが可能です。

#### コンテキスト

コンテキストは、Serenaが動作する一般的な環境を定義します。
これは、初期のシステムプロンプトと利用可能なツールのセットに影響します。
コンテキストは、Serenaの起動時に設定され（例：MCPサーバーのCLIオプションまたはエージェントスクリプト内）、アクティブなセッション中には変更できません。

Serenaには、事前定義されたコンテキストが付属しています：

* `desktop-app`: Claude Desktopなどのデスクトップアプリケーションでの使用に合わせて調整されています。これがデフォルトです。
* `agent`: Serenaがより自律的なエージェントとして機能するシナリオ向けに設計されています。たとえば、Agnoと使用する場合などです。
* `ide-assistant`: VSCode、Cursor、ClineなどのIDEへの統合に最適化されており、エディター内でのコーディング支援に焦点を当てています。
使用している統合のタイプに最も一致するコンテキストを選択してください。

Serenaを起動するときは、`--context <context-name>`を使用してコンテキストを指定します。
パラメータリストが指定されている場合（例：Claude Desktop）、リストに2つのパラメータを追加する必要があることに注意してください。

OpenAI互換のツール記述を使用する必要があるローカルサーバー（Llama.cppなど）を使用していて、`agent`の代わりにコンテキスト`oaicompat-agent`を使用してください。

#### モード

モードは、特定の種類のタスクや対話スタイルに合わせてSerenaの動作をさらに調整します。複数のモードを同時にアクティブにすることができ、それらの効果を組み合わせることができます。モードはシステムプロンプトに影響を与え、特定のツールを除外することで利用可能なツールのセットを変更することもできます。

組み込みモードの例は次のとおりです：

* `planning`: Serenaを計画および分析タスクに集中させます。
* `editing`: Serenaを直接的なコード変更タスクに最適化します。
* `interactive`: 会話形式のやり取りに適しています。
* `one-shot`: 1回の応答で完了する必要があるタスク用にSerenaを設定します。レポートや初期計画の生成に`planning`とともによく使用されます。
* `no-onboarding`: 特定のセッションで不要な場合、初期のオンボーディングプロセスをスキップします。
* `onboarding`: （通常は自動的にトリガーされます）プロジェクトのオンボーディングプロセスに焦点を当てます。

モードは起動時に（コンテキストと同様に）設定できますが、セッション中に_動的に切り替える_こともできます。LLMに`switch_modes`ツールを使用して別のモードセットをアクティブにするように指示できます（例：「planningモードとone-shotモードに切り替えて」）。

Serenaを起動するときは、`--mode <mode-name>`を使用してモードを指定します。複数のモードを指定できます。例：`--mode planning --mode no-onboarding`。

:warning: **モードの互換性**: モードを組み合わせることはできますが、一部は意味的に互換性がない場合があります（例：`interactive`と`one-shot`）。Serenaは現在、互換性のない組み合わせを防ぎません。賢明なモード構成を選択するのはユーザー次第です。

#### カスタマイズ

独自のコンテキストとモードを作成して、Serenaをニーズに正確に合わせることができます。これには2つの方法があります。

* SerenaのCLIを使用してモードとコンテキストを管理できます。以下を確認してください。

    ```shell
    uvx --from git+https://github.com/oraios/serena serena mode --help
    ```

    および

    ```shell
    uvx --from git+https://github.com/oraios/serena serena context --help
    ```

    _注意_: カスタムコンテキスト/モードは、`<home>/.serena`内の単なるYAMLファイルです。これらは自動的に登録され、名前（`.yml`拡張子なしのファイル名）で使用できます。SerenaのCLIを使用したくない場合は、任意の方法で作成および管理できます。
* **外部YAMLファイルの使用**: Serenaを起動するときに、コンテキストまたはモードのカスタム`.yml`ファイルへの絶対パスを指定することもできます。

このカスタマイズにより、Serenaを特定のプロジェクト要件や個人の好みに合わせて深く統合および適応させることができます。

### オンボーディングとメモリ

デフォルトでは、Serenaはプロジェクトで初めて起動されたときに**オンボーディングプロセス**を実行します。
オンボーディングの目標は、Serenaがプロジェクトに慣れ、将来の対話で利用できるメモリを保存することです。
LLMがオンボーディングを完了できず、実際に対応するメモリをディスクに書き込まなかった場合は、明示的にそうするように依頼する必要がある場合があります。

オンボーディングでは通常、プロジェクトから多くのコンテンツを読み取るため、コンテキストがいっぱいになります。
したがって、オンボーディングが完了したら、別の会話に切り替えることをお勧めします。
オンボーディング後、メモリをざっと見て、必要に応じて編集したり、追加のメモリを追加したりすることをお勧めします。

**メモリ**は、プロジェクトディレクトリの`.serena/memories/`に保存されているファイルで、エージェントは後続の対話で読み取ることを選択できます。
必要に応じて自由に読み取り、調整してください。手動で新しいものを追加することもできます。
`.serena/memories/`ディレクトリ内のすべてのファイルがメモリファイルです。
Serenaがプロジェクトで作業を開始するたびに、メモリのリストが提供され、エージェントはそれらを読み取ることを決定できます。
メモリはSerenaのユーザーエクスペリエンスを大幅に向上させることがわかりました。

### プロジェクトの準備

#### コードベースの構造化

Serenaは、コードの検索、読み取り、編集にコード構造を使用します。これは、
適切に構造化されたコードではうまく機能しますが、完全に非構造化されたコード（巨大で非モジュールな関数を持つ「Godクラス」など）ではパフォーマンスが低下する可能性があります。
さらに、静的に型付けされていない言語では、型アノテーションが非常に有益です。

#### クリーンな状態から始める

コード生成タスクは、クリーンなgit状態から開始するのが最善です。これにより、変更内容を簡単に追跡し、問題が発生した場合に元に戻すことができます。

この機能は、デリバティブ取引や金融市場向けの自動売買戦略の開発に大きな変革をもたらす可能性を秘めています。

### ライセンスについて

このプロジェクトのコア部分は[MITライセンス](LICENSE)の下で公開されていますが、私（khayashi4337）が開発したMQL5サポート機能については、デュアルライセンスモデルを適用します。

*   **非商用利用**の場合は、オープンソースライセンスの下で無償でご利用いただけます。
*   **商用利用**を目的とされる場合は、別途商用ライセンスの契約が必要です。

商用ライセンスに関するご相談やお問い合わせは、<khayashi4337@gmail.com> までご連絡ください。

## 目次

<!-- Created with markdown-toc -i README.md -->
<!-- Install it with npm install -g markdown-toc -->

<!-- toc -->

- [目次](#目次)
- [クイックスタート](#クイックスタート)
  - [Serena MCPサーバーの実行](#serena-mcpサーバーの実行)
    - [使用方法](#使用方法)
      - [uvxの使用](#uvxの使用)
        - [ローカルインストール](#ローカルインストール)
      - [Dockerの使用（実験的）](#dockerの使用実験的)
    - [SSEモード](#sseモード)
    - [コマンドライン引数](#コマンドライン引数)
  - [設定](#設定)
  - [プロジェクトのアクティベーションとインデックス作成](#プロジェクトのアクティベーションとインデックス作成)
  - [Claude Code](#claude-code)
  - [Codex](#codex)
  - [その他のターミナルベースのクライアント](#その他のターミナルベースのクライアント)
  - [Claude Desktop](#claude-desktop)
  - [MCPコーディングクライアント（Cline、Roo-Code、Cursor、Windsurfなど）](#mcpコーディングクライアントclineroo-codecursorwindsurfなど)
  - [ローカルGUIとフレームワーク](#ローカルguiとフレームワーク)
- [詳細な使用方法と推奨事項](#詳細な使用方法と推奨事項)
  - [ツールの実行](#ツールの実行)
    - [シェル実行と編集ツール](#シェル実行と編集ツール)
  - [モードとコンテキスト](#モードとコンテキスト)
    - [コンテキスト](#コンテキスト)
    - [モード](#モード)
    - [カスタマイズ](#カスタマイズ)
  - [オンボーディングとメモリ](#オンボーディングとメモリ)
  - [プロジェクトの準備](#プロジェクトの準備)
    - [コードベースの構造化](#コードベースの構造化)
    - [クリーンな状態から始める](#クリーンな状態から始める)

<!-- tocstop -->
