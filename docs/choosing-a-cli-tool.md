# Choosing a CLI Tool

How to pick the right command-line tool without regretting it later.

## 1. Install from your package manager first

Prefer `brew`, `apt`/`dnf`/`pacman`, `winget`, or `cargo install`/`go install` over `curl | sh` installers. Package-manager versions are checksummed, updatable, and removable. Only fall back to a GitHub release binary when your manager doesn't carry the tool.

## 2. Check maintenance, not just stars

Stars measure popularity, not health. Before adopting a tool, glance at the repo: commits in the last 6–12 months, open issues getting maintainer replies, and a CI badge that's green. This list marks each entry's status (`active`, `maintenance`, `archived`) as of 2026-09-30 — re-check before depending on anything critical.

## 3. Read the license before you ship it

MIT/Apache-2.0/BSD tools can be embedded anywhere. GPL/AGPL tools are fine to *use*, but think twice before bundling them into a product you distribute. Every entry in this list links its verified license — `⚠️ license unverified` means we could not confirm it, not that it's permissive.

## 4. Match the tool to the job

- **Interactive daily driver** (file manager, git TUI, editor): pick the one whose keybindings you'll actually learn. Try two for a week each.
- **Scripting/pipelines**: prefer tools with stable, machine-readable output (`--json` flags, no color codes on pipes). `jq`, `yq`, `miller`, and `dasel` exist for exactly this.
- **One-off tasks**: `tldr`/`tealdeer` beats reading full man pages.

## 5. Mind the platform

Most tools here build on Linux, macOS, and Windows, but not all — check the `platforms` field in `data/cli.json`. Windows users: prefer tools with native builds over WSL-only ones when scripting for others.

## 6. Dotfiles are the real product

The tool is 20% of the value; your config is the other 80%. Keep shell and tool configs in version control from day one.
