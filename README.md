# Awesome OSS CLI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **102 open-source command-line tools** — shells, file managers, search, git TUIs, monitoring, networking, data wrangling, and more. Every entry links to its source repository, and every license was checked against the project's official license file or metadata on 2026-09-30.

- ✅ **101/102** licenses verified from official sources
- 🖥️ Linux-first catalog; most tools also build on macOS and Windows — see the data file for per-tool platforms
- 📦 Machine-readable data in [`data/cli.json`](data/cli.json)

## Contents

- [🐚 Shells & Prompts](#shells--prompts) (9)
- [🪟 Terminal Multiplexers](#terminal-multiplexers) (5)
- [📁 File Managers & Navigation](#file-managers--navigation) (11)
- [🔍 Search & Find](#search--find) (6)
- [🌿 Git & Version Control](#git--version-control) (9)
- [✏️ Terminal Editors](#terminal-editors) (4)
- [📊 System Monitoring](#system-monitoring) (11)
- [🌐 Networking & HTTP](#networking--http) (11)
- [🗄️ Data Tools](#data-tools) (10)
- [📝 Text Processing](#text-processing) (6)
- [🎬 Media](#media) (6)
- [⚡ Productivity & Misc](#productivity--misc) (14)
- [Notable exclusions](#notable-exclusions)
- [Related](#related)
- [Contributing](#contributing)
- [License](#license)

## 🐚 Shells & Prompts

Interactive shells, prompts, and shell enhancements.

- **[atuin](https://github.com/atuinsh/atuin)** — Magical shell history with sync, search, and stats. [`MIT`](https://github.com/atuinsh/atuin/blob/HEAD/LICENSE) · [website](https://atuin.sh)
- **[elvish](https://github.com/elves/elvish)** — Expressive functional shell with structured data. [`BSD-2-Clause`](https://github.com/elves/elvish) · [website](https://elv.sh/)
- **[fish](https://github.com/fish-shell/fish-shell)** — User-friendly interactive command-line shell. [`GPL-2.0-only`](https://github.com/fish-shell/fish-shell/blob/HEAD/COPYING) · [website](https://fishshell.com)
- **[nushell](https://github.com/nushell/nushell)** — Modern structured-data shell with typed pipelines. [`MIT`](https://github.com/nushell/nushell) · [website](https://www.nushell.sh/)
- **[oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh)** — Community-driven framework for managing zsh configuration. [`MIT`](https://github.com/ohmyzsh/ohmyzsh) · [website](https://ohmyz.sh)
- **[powerlevel10k](https://github.com/romkatv/powerlevel10k)** — Fast, flexible zsh prompt theme. [`MIT`](https://github.com/romkatv/powerlevel10k)
- **[starship](https://github.com/starship/starship)** — Minimal, fast, customizable cross-shell prompt. [`ISC`](https://github.com/starship/starship) · [website](https://starship.rs)
- **[zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)** — Fish-like autosuggestions for zsh. [`MIT`](https://github.com/zsh-users/zsh-autosuggestions)
- **[zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)** — Fish-like syntax highlighting for zsh. [`BSD-3-Clause`](https://github.com/zsh-users/zsh-syntax-highlighting)

## 🪟 Terminal Multiplexers

Split panes, sessions, and persistent terminal workspaces.

- **[abduco](https://github.com/martanne/abduco)** — Session attach/detach tool (like dtach). [`ISC`](https://github.com/martanne/abduco)
- **[byobu](https://github.com/dustinkirkland/byobu)** — User-friendly profile and window manager for tmux/screen. [`GPL-3.0-only`](https://github.com/dustinkirkland/byobu) · [website](https://byobu.org)
- **[dvtm](https://github.com/martanne/dvtm)** — Tiling window manager for the console. [`MIT`](https://github.com/martanne/dvtm)
- **[tmux](https://github.com/tmux/tmux)** — Terminal multiplexer: windows, panes, and session persistence. [`ISC`](https://github.com/tmux/tmux)
- **[zellij](https://github.com/zellij-org/zellij)** — Modern terminal workspace with panes, tabs, and plugins. [`MIT`](https://github.com/zellij-org/zellij) · [website](https://zellij.dev)

## 📁 File Managers & Navigation

Navigate, preview, and manage files without leaving the terminal.

- **[broot](https://github.com/Canop/broot)** — Fuzzy file navigator and directory tree explorer. [`MIT`](https://github.com/Canop/broot) · [website](https://dystroy.org/broot)
- **[dua-cli](https://github.com/Byron/dua-cli)** — Interactive disk-usage analyzer with delete support. [`MIT`](https://github.com/Byron/dua-cli)
- **[dust](https://github.com/bootandy/dust)** — Intuitive visual du: disk usage at a glance. [`Apache-2.0`](https://github.com/bootandy/dust)
- **[eza](https://github.com/eza-community/eza)** — Modern replacement for ls with colors and git integration. [`EUPL-1.2`](https://github.com/eza-community/eza) · [website](https://eza.rocks)
- **[fzf](https://github.com/junegunn/fzf)** — General-purpose fuzzy finder for the command line. [`MIT`](https://github.com/junegunn/fzf) · [website](https://junegunn.github.io/fzf/)
- **[lf](https://github.com/gokcehan/lf)** — Minimal terminal file manager written in Go. [`MIT`](https://github.com/gokcehan/lf)
- **[nnn](https://github.com/jarun/nnn)** — Tiny, fast, full-featured terminal file manager. [`BSD-2-Clause`](https://github.com/jarun/nnn)
- **[ranger](https://github.com/ranger/ranger)** — Vim-inspired console file manager with previews. [`GPL-3.0-only`](https://github.com/ranger/ranger) · [website](https://ranger.fm)
- **[xplr](https://github.com/sayanarijit/xplr)** — Hackable terminal file explorer with Lua plugins. [`MIT`](https://github.com/sayanarijit/xplr) · [website](https://xplr.dev)
- **[yazi](https://github.com/sxyazi/yazi)** — Blazing-fast terminal file manager with image previews. [`MIT`](https://github.com/sxyazi/yazi) · [website](https://yazi-rs.github.io)
- **[zoxide](https://github.com/ajeetdsouza/zoxide)** — Smarter cd: frecency-based directory jumper. [`MIT`](https://github.com/ajeetdsouza/zoxide)

## 🔍 Search & Find

Blazing-fast text search, file finding, and fuzzy matching.

- **[fd](https://github.com/sharkdp/fd)** — Simple, fast alternative to find. [`Apache-2.0`](https://github.com/sharkdp/fd)
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — Extremely fast recursive grep alternative (rg). [`Unlicense`](https://github.com/BurntSushi/ripgrep)
- **[ripgrep-all](https://github.com/phiresky/ripgrep-all)** — ripgrep that also searches PDFs, archives, and docs (rga). [`AGPL-3.0-only`](https://github.com/phiresky/ripgrep-all/blob/HEAD/LICENSE.md)
- **[skim](https://github.com/skim-rs/skim)** — Fuzzy finder in Rust (fzf-like). [`MIT`](https://github.com/skim-rs/skim)
- **[the_silver_searcher](https://github.com/ggreer/the_silver_searcher)** — Fast code-searching tool (ag). [`Apache-2.0`](https://github.com/ggreer/the_silver_searcher) · [website](https://geoff.greer.fm/ag/)
- **[ugrep](https://github.com/Genivia/ugrep)** — Ultra-fast grep with fuzzy and boolean search. [`BSD-3-Clause`](https://github.com/Genivia/ugrep) · [website](https://ugrep.com)

## 🌿 Git & Version Control

Git TUIs, diffs, and repository insight tools.

- **[delta](https://github.com/dandavison/delta)** — Syntax-highlighting pager for git and diff output. [`MIT`](https://github.com/dandavison/delta) · [website](https://dandavison.github.io/delta/)
- **[gh](https://github.com/cli/cli)** — GitHub's official command-line tool. [`MIT`](https://github.com/cli/cli) · [website](https://cli.github.com)
- **[git-absorb](https://github.com/tummychow/git-absorb)** — Automatically absorb staged changes into fixup commits. [`BSD-3-Clause`](https://github.com/tummychow/git-absorb)
- **[git-extras](https://github.com/tj/git-extras)** — Extra git commands for everyday workflow. [`MIT`](https://github.com/tj/git-extras)
- **[gitu](https://github.com/altsem/gitu)** — Magit-inspired TUI git client. [`MIT`](https://github.com/altsem/gitu)
- **[gitui](https://github.com/gitui-org/gitui)** — Blazing-fast terminal UI for git written in Rust. [`MIT`](https://github.com/gitui-org/gitui)
- **[lazygit](https://github.com/jesseduffield/lazygit)** — Simple terminal UI for git commands. [`MIT`](https://github.com/jesseduffield/lazygit)
- **[onefetch](https://github.com/o2sh/onefetch)** — Neofetch-style git repository summary. [`MIT`](https://github.com/o2sh/onefetch) · [website](https://onefetch.dev)
- **[tig](https://github.com/jonas/tig)** — Text-mode interface for git. [`GPL-2.0-only`](https://github.com/jonas/tig) · [website](https://jonas.github.io/tig/)

## ✏️ Terminal Editors

Modal and modern editors that live in the terminal.

- **[helix](https://github.com/helix-editor/helix)** — Modal text editor with built-in LSP and tree-sitter. [`MPL-2.0`](https://github.com/helix-editor/helix) · [website](https://helix-editor.com)
- **[kakoune](https://github.com/mawww/kakoune)** — Modal editor with multiple selections as the core interaction. [`Unlicense`](https://github.com/mawww/kakoune) · [website](https://kakoune.org)
- **[micro](https://github.com/micro-editor/micro)** — Modern, intuitive terminal text editor. [`MIT`](https://github.com/micro-editor/micro) · [website](https://micro-editor.github.io)
- **[neovim](https://github.com/neovim/neovim)** — Hyperextensible Vim-based text editor. [`Apache-2.0`](https://github.com/neovim/neovim/blob/HEAD/LICENSE.txt) · [website](https://neovim.io)

## 📊 System Monitoring

Processes, resources, disks, and network usage at a glance.

- **[bandwhich](https://github.com/imsnif/bandwhich)** — Terminal bandwidth utilization monitor. [`MIT`](https://github.com/imsnif/bandwhich)
- **[bottom](https://github.com/ClementTsang/bottom)** — Customizable graphical process and system monitor (btm). [`MIT`](https://github.com/ClementTsang/bottom) · [website](https://bottom.pages.dev)
- **[btop](https://github.com/aristocratos/btop)** — Resource monitor with a game-inspired theme. [`Apache-2.0`](https://github.com/aristocratos/btop)
- **[doggo](https://github.com/mr-karan/doggo)** — User-friendly command-line DNS client. [`GPL-3.0-only`](https://github.com/mr-karan/doggo) · [website](https://doggo.mrkaran.dev/)
- **[duf](https://github.com/muesli/duf)** — Disk usage/free utility with a polished UI. [`MIT`](https://github.com/muesli/duf/blob/HEAD/LICENSE)
- **[glances](https://github.com/nicolargo/glances)** — Cross-platform system monitoring tool (CLI and web). [`LGPL-3.0-only`](https://github.com/nicolargo/glances/blob/HEAD/COPYING) · [website](https://nicolargo.github.io/glances/)
- **[gping](https://github.com/orf/gping)** — Ping with a live TUI graph. [`MIT`](https://github.com/orf/gping)
- **[htop](https://github.com/htop-dev/htop)** — Interactive process viewer. [`GPL-2.0-or-later`](https://github.com/htop-dev/htop) · [website](https://htop.dev/)
- **[nvitop](https://github.com/XuehaiPan/nvitop)** — Interactive NVIDIA GPU process viewer and monitor. [`Apache-2.0`](https://github.com/XuehaiPan/nvitop) · [website](https://nvitop.readthedocs.io)
- **[nvtop](https://github.com/Syllo/nvtop)** — GPU and accelerator process monitor (htop-like). [`GPL-3.0-only`](https://github.com/Syllo/nvtop/blob/HEAD/COPYING)
- **[procs](https://github.com/dalance/procs)** — Modern replacement for ps. [`MIT`](https://github.com/dalance/procs)

## 🌐 Networking & HTTP

HTTP clients, DNS tools, load testing, and packet inspection.

- **[aria2](https://github.com/aria2/aria2)** — Lightweight multi-protocol download utility. [`GPL-2.0-only`](https://github.com/aria2/aria2) · [website](https://aria2.github.io/)
- **[curl](https://github.com/curl/curl)** — Command-line tool for transferring data with URLs. [`curl`](https://github.com/curl/curl/blob/HEAD/COPYING) · [website](https://curl.se/)
- **[dog](https://github.com/ogham/dog)** — Command-line DNS client with a modern UX. [`EUPL-1.2`](https://github.com/ogham/dog) · [website](https://dns.lookup.dog/)
- **[httpie](https://github.com/httpie/cli)** — Human-friendly HTTP client for APIs. [`BSD-3-Clause`](https://github.com/httpie/cli) · [website](https://httpie.io)
- **[mosh](https://github.com/mobile-shell/mosh)** — Mobile shell: roaming, intermittent-connectivity SSH replacement. [`GPL-3.0-only`](https://github.com/mobile-shell/mosh) · [website](https://mosh.org)
- **[mtr](https://github.com/traviscross/mtr)** — Network diagnostic combining ping and traceroute. [`GPL-2.0-only`](https://github.com/traviscross/mtr) · [website](https://www.bitwizard.nl/mtr/)
- **[oha](https://github.com/hatoo/oha)** — HTTP load generator inspired by hey. [`MIT`](https://github.com/hatoo/oha)
- **[termshark](https://github.com/gcla/termshark)** — Terminal UI for tshark (Wireshark for the console). [`MIT`](https://github.com/gcla/termshark)
- **[trippy](https://github.com/fujiapple852/trippy)** — Network diagnostic tool with a polished TUI (trip). [`Apache-2.0`](https://github.com/fujiapple852/trippy) · [website](https://trippy.rs)
- **[wrk](https://github.com/wg/wrk)** — Modern HTTP benchmarking tool. [`Apache-2.0`](https://github.com/wg/wrk/blob/HEAD/LICENSE)
- **[xh](https://github.com/ducaale/xh)** — Friendly fast HTTP client reimplemented in Rust. [`MIT`](https://github.com/ducaale/xh)

## 🗄️ Data Tools

Slice, query, and reshape JSON, YAML, CSV, and SQL from the shell.

- **[csvkit](https://github.com/wireservice/csvkit)** — Suite of utilities for working with CSV files. [`MIT`](https://github.com/wireservice/csvkit) · [website](https://csvkit.readthedocs.io)
- **[dasel](https://github.com/TomWright/dasel)** — Query and modify JSON, YAML, TOML, XML, and CSV. [`MIT`](https://github.com/TomWright/dasel) · [website](https://daseldocs.tomwright.me)
- **[duckdb](https://github.com/duckdb/duckdb)** — In-process analytical SQL database with a CLI. [`MIT`](https://github.com/duckdb/duckdb) · [website](https://www.duckdb.org)
- **[fx](https://github.com/antonmedv/fx)** — Terminal JSON viewer with interactive exploration. [`MIT`](https://github.com/antonmedv/fx) · [website](https://fx.wtf)
- **[jq](https://github.com/jqlang/jq)** — Lightweight command-line JSON processor. [`MIT`](https://github.com/jqlang/jq/blob/HEAD/COPYING) · [website](https://jqlang.org)
- **[miller](https://github.com/johnkerl/miller)** — Like awk/sed/cut/join for CSV, TSV, and JSON (mlr). [`BSD-2-Clause`](https://github.com/johnkerl/miller/blob/HEAD/LICENSE.txt) · [website](https://miller.readthedocs.io)
- **[sqlite](https://github.com/sqlite/sqlite)** — Self-contained SQL database engine with an interactive CLI shell. ⚠️ `license unverified` · [website](https://sqlite.org)
- **[usql](https://github.com/xo/usql)** — Universal command-line interface for SQL databases. [`MIT`](https://github.com/xo/usql)
- **[visidata](https://github.com/saulpw/visidata)** — Terminal spreadsheet for exploring tabular data. [`GPL-3.0-only`](https://github.com/saulpw/visidata) · [website](https://visidata.org)
- **[yq](https://github.com/mikefarah/yq)** — Portable command-line YAML, JSON, and XML processor. [`MIT`](https://github.com/mikefarah/yq) · [website](https://mikefarah.gitbook.io/yq/)

## 📝 Text Processing

Render, convert, and transform text and documents.

- **[bat](https://github.com/sharkdp/bat)** — cat clone with syntax highlighting and git integration. [`Apache-2.0`](https://github.com/sharkdp/bat)
- **[choose](https://github.com/theryangeary/choose)** — Human-friendly cut/awk alternative for field selection. [`GPL-3.0-only`](https://github.com/theryangeary/choose)
- **[glow](https://github.com/charmbracelet/glow)** — Render markdown beautifully in the terminal. [`MIT`](https://github.com/charmbracelet/glow)
- **[mdcat](https://github.com/swsnr/mdcat)** — Fancy cat for Markdown with syntax highlighting. [`MPL-2.0`](https://github.com/swsnr/mdcat)
- **[pandoc](https://github.com/jgm/pandoc)** — Universal document converter (markdown, HTML, LaTeX, ...). [`GPL-2.0-only`](https://github.com/jgm/pandoc) · [website](https://pandoc.org)
- **[sd](https://github.com/chmln/sd)** — Intuitive find-and-replace CLI (sed alternative). [`MIT`](https://github.com/chmln/sd)

## 🎬 Media

Download, convert, and preview media from the command line.

- **[chafa](https://github.com/hpjansson/chafa)** — Terminal graphics: images and video as text/sixels. [`LGPL-3.0-only`](https://github.com/hpjansson/chafa) · [website](https://hpjansson.org/chafa/)
- **[ffmpeg](https://github.com/FFmpeg/FFmpeg)** — Complete solution to record, convert, and stream media. [`LGPL-2.1-or-later`](https://github.com/FFmpeg/FFmpeg/blob/HEAD/LICENSE.md) · [website](https://ffmpeg.org/)
- **[imagemagick](https://github.com/ImageMagick/ImageMagick)** — Create, edit, compose, and convert images from the CLI. [`ImageMagick`](https://github.com/ImageMagick/ImageMagick/blob/HEAD/LICENSE) · [website](https://imagemagick.org)
- **[timg](https://github.com/hzeller/timg)** — Terminal image and video viewer. [`GPL-2.0-only`](https://github.com/hzeller/timg)
- **[viu](https://github.com/atanunq/viu)** — Terminal image viewer with iTerm/Kitty graphics support. [`MIT`](https://github.com/atanunq/viu)
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Feature-rich command-line video/audio downloader. [`Unlicense`](https://github.com/yt-dlp/yt-dlp)

## ⚡ Productivity & Misc

Tasks, notes, timers, and everyday terminal utilities.

- **[direnv](https://github.com/direnv/direnv)** — Per-directory environment variable management. [`MIT`](https://github.com/direnv/direnv) · [website](https://direnv.net)
- **[entr](https://github.com/eradman/entr)** — Run arbitrary commands when files change. [`ISC`](https://github.com/eradman/entr/blob/HEAD/LICENSE) · [website](https://eradman.com/entrproject/)
- **[gum](https://github.com/charmbracelet/gum)** — Glamorous shell scripts: prompts, spinners, and TUIs. [`MIT`](https://github.com/charmbracelet/gum)
- **[hyperfine](https://github.com/sharkdp/hyperfine)** — Command-line benchmarking tool. [`Apache-2.0`](https://github.com/sharkdp/hyperfine)
- **[just](https://github.com/casey/just)** — Handy command runner (make-like, without the pain). [`CC0-1.0`](https://github.com/casey/just) · [website](https://just.systems)
- **[mods](https://github.com/charmbracelet/mods)** — AI on the command line (stdin-powered LLM pipelines). [`MIT`](https://github.com/charmbracelet/mods)
- **[navi](https://github.com/denisidoro/navi)** — Interactive cheatsheet tool for the command line. [`Apache-2.0`](https://github.com/denisidoro/navi)
- **[skate](https://github.com/charmbracelet/skate)** — Personal key-value store with sync. [`MIT`](https://github.com/charmbracelet/skate)
- **[soft-serve](https://github.com/charmbracelet/soft-serve)** — Self-hostable Git server with a TUI over SSH. [`MIT`](https://github.com/charmbracelet/soft-serve)
- **[taskwarrior](https://github.com/GothenburgBitFactory/taskwarrior)** — Command-line task and todo manager. [`MIT`](https://github.com/GothenburgBitFactory/taskwarrior) · [website](https://taskwarrior.org)
- **[tealdeer](https://github.com/tealdeer-rs/tealdeer)** — Fast tldr client with syntax-highlighted cheatsheets. [`Apache-2.0`](https://github.com/tealdeer-rs/tealdeer) · [website](https://docs.tealdeer.org)
- **[tldr](https://github.com/tldr-pages/tldr)** — Community-maintained cheatsheets; official reference Python client. [`CC-BY-4.0`](https://github.com/tldr-pages/tldr/blob/HEAD/LICENSE.md) · [website](https://tldr.sh)
- **[tokei](https://github.com/XAMPPRocky/tokei)** — Count code lines, comments, and blanks blazingly fast. [`MIT OR Apache-2.0`](https://github.com/XAMPPRocky/tokei/blob/HEAD/LICENCE-MIT)
- **[vhs](https://github.com/charmbracelet/vhs)** — Generate terminal GIFs and videos from code. [`MIT`](https://github.com/charmbracelet/vhs)

## Notable exclusions

Popular terminal tools deliberately left out because they are not open source, are unmaintained, or are superseded:

- **1Password CLI (`op`), Bitwarden CLI (`bw`)** — proprietary (Bitwarden server is OSS; the CLI clients are not fully open).
- **Warp, Fig/Amazon Q developer CLI autocomplete** — proprietary.
- **exa** — unmaintained and archived by its author; superseded by **eza** (listed above).
- **gtop** — unmaintained for years; use **btop** or **bottom** instead.
- Tools whose license could not be confirmed on any official source are omitted rather than listed with a guessed license.

## Related

- [Awesome OSS macOS](https://github.com/Awesome-llms-labs/awesome-oss-macos) — open-source macOS applications (sibling list).
- [Awesome AI Agents](https://github.com/dakotac1994/awesome-ai-agents) — the AI agent ecosystem.
- [Awesome Jev](https://github.com/dakotac1994/awesome-jev) — TypeSafe's Jev / System One.

## Documentation

- [Choosing a CLI tool](docs/choosing-a-cli-tool.md)
- [Glossary](docs/glossary.md)
- [Status changes](docs/status-changes.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New entries must be open-source licensed, runnable from a terminal, and verifiable via a public Git repository.

## License

This list is released under the [MIT License](LICENSE).
