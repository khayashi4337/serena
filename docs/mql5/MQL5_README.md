# MQL5
MQL5のLSP用にいくつか、forkしてリポジトリを作ってきました。

## khayashi4337/mql5: C++用LSP(clangd)をMQL5用に設定するためのアダプターです。
## khayashi4337/tree-sitter-mql5: MQL5の構文解析器（パーサー）であり、LSPとは直接関係ありません。

mql5_server.pyで実装しています。

# MQL5 Language Server Support in Serena

This document outlines how MQL5 language support is implemented in Serena.

## Summary

Serena provides Language Server Protocol (LSP) support for MQL5 by leveraging `clangd`, a mature C++ language server. This is achieved through a custom adapter that configures `clangd` to correctly interpret MQL5 syntax.

The necessary setup, including fetching required header files and generating configuration, is handled **automatically** by Serena.

## Key Components

*   **`khayashi4337/mql5`**: A forked repository containing MQL5-specific header files. Serena automatically clones this repository and uses it to configure `clangd`.
*   **`khayashi4337/tree-sitter-mql5`**: A tree-sitter parser for MQL5 syntax. This is not directly used by the LSP but is available for other features like syntax highlighting.

## Implementation

The core logic is implemented in `src/solidlsp/language_servers/mql5_server.py`. This server class inherits from `ClangdLanguageServer` and handles the MQL5-specific setup process.
