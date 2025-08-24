# serenaのLSP機能の構造


```
  serena (アプリケーション本体)
    │
    └─> solidlsp (LSP機能の管理モジュール)
         │
         ├─> SolidLanguageServer (ls.py): 全言語共通のインターフェース
         │
         └─> PyrightServer (pyright_server.py): Python固有の実装
              │
              └─> (OSの別プロセスとして起動)
                   │
                   └─> Pyright Language Server: 実際のPythonコード分析を行う
```

このアーキテクチャの利点は、言語ごとにパーサーを自前で実装する（例えばtree-sitterで一から作る）必要がなく、各言語で最も強力なツールを再利用できる点にあります。これにより、多くの言語を効率的にサポートすることが可能になっています。