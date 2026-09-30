# Glossary

- **CLI** — Command-Line Interface: a program you drive by typing commands and flags.
- **TUI** — Text/Terminal User Interface: a full-screen, keyboard-driven interface drawn with text (e.g. `lazygit`, `btop`).
- **REPL** — Read–Eval–Print Loop: an interactive prompt that evaluates each line (e.g. `sqlite3`, `duckdb`).
- **Pager** — a program that shows long output one screen at a time (`less`, `bat`).
- **Fuzzy finder** — interactive search that matches partial/approximate input (`fzf`, `skim`).
- **Multiplexer** — keeps terminal sessions alive and splits them into panes/windows (`tmux`, `zellij`).
- **Dotfiles** — your shell and tool configuration files, usually kept in `~` and version-controlled.
- **POSIX** — the portable shell standard (`sh`); `bash`/`zsh`/`fish` extend it to varying degrees.
- **Man page** — the built-in Unix manual (`man rg`); `tldr` gives community cheat-sheet versions.
- **STDIN / STDOUT / STDERR** — the three standard streams; Unix tools compose by piping STDOUT into the next tool's STDIN.
- **Exit code** — the number a program returns on exit; `0` means success.
