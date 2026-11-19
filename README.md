# 🍙 dotfiles

[![Arch Linux](https://img.shields.io/badge/OS-Arch%20Linux-blue?logo=arch-linux&logoColor=white)](https://archlinux.org)
[![Hyprland](https://img.shields.io/badge/WM-Hyprland%20(Lua)-00c8ff?logo=wayland&logoColor=white)](https://hyprland.org)
[![Chezmoi](https://img.shields.io/badge/Managed%20with-Chezmoi-orange?logo=chezmoi&logoColor=white)](https://chezmoi.io)
[![Neovim](https://img.shields.io/badge/Editor-Neovim%20(LazyVim)-green?logo=neovim&logoColor=white)](https://neovim.io)
[![Kitty](https://img.shields.io/badge/Terminal-Kitty-yellow?logo=kitty&logoColor=white)](https://sw.kovidgoyal.net/kitty/)

Personal Wayland desktop dotfiles for **Arch Linux** and **CachyOS**, managed with [chezmoi](https://www.chezmoi.io/). Designed with a minimalist OLED-black aesthetic (*Ashen Dark*), modular Lua configurations, and a keyboard-centric tiling workflow.

---

## 📑 Table of Contents

- [Highlights](#-highlights)
- [Component Stack](#-component-stack)
- [Installation & Bootstrap](#-installation--bootstrap)
- [Core Keybindings](#-core-keybindings)
- [Centralized Theming](#-centralized-theming)
- [Repository Structure](#-repository-structure)
- [Post-Install Tips & Addons](#-post-install-tips--addons)

---

## ✨ Highlights

* **Centralized Ashen Theme Engine:** A single configuration file (`.chezmoidata/theme-colors.toml`) controls color tokens for Hyprland, Waybar, Kitty, Dunst, Walker, Neovim, Zathura, and Xournal++. Changing values triggers a live reload of all active GUI components without session restarts.
* **Hyprland in Lua:** Configured using Hyprland's native Lua module system (`hyprland.lua`) with clean separation into `monitors`, `bindings`, `workspaces`, `looknfeel`, and `autostart`.
* **Dynamic Waybar Group-Tabs:** Custom Python daemon (`waybar-group-tabs`) providing real-time tab status, scrolling navigation, and a quick-select menu for grouped/tabbed windows.
* **Context-Aware Keybinding Helper:** Interactive launcher (`showkeybindings`) that detects the active window (Neovim, Yazi, Zathura, or Hyprland) and presents applicable keybindings in Walker.
* **Custom XKB Symbols:** Tailored keyboard symbols (`gb_umlauts` and `us_umlauts`) providing UK and US layouts with German umlaut mapping via AltGr.
* **Automated Bootstrapping:** Self-executing lifecycle scripts install system packages (`pacman` and `yay`), set up Oh-My-Zsh, configure standalone IWD Wi-Fi, and deploy developer tools on initial deployment.

---

## 🛠 Component Stack

| Category | Component | Purpose |
| :--- | :--- | :--- |
| **Compositor** | [Hyprland](https://hyprland.org/) | Dynamic Wayland tiling window manager |
| **Status Bar** | [Waybar](https://github.com/Alexays/Waybar) | Top panel with workspaces, system metrics, group tabs, and Tailscale |
| **Launcher** | [Walker](https://github.com/abenz1267/walker) + [Elephant](https://github.com/abenz1267/elephant) | Application runner, clipboard manager, and dmenu provider |
| **Terminal** | [Kitty](https://sw.kovidgoyal.net/kitty/) | GPU-accelerated terminal with Ashen dark palette |
| **Shell** | [Zsh](https://www.zsh.org/) + [Oh-My-Zsh](https://ohmyz.sh/) | Fast command line with custom `dog` prompt and [zoxide](https://github.com/ajeetdsouza/zoxide) |
| **Editor** | [Neovim](https://neovim.io/) + [LazyVim](https://www.lazyvim.org/) | Extensible editor with Neo-tree, window navigation, VimTeX, and PlatformIO |
| **File Manager** | [Yazi](https://yazi-rs.github.io/) | Terminal file manager with `wayclip` system clipboard integration |
| **Document Viewer** | [Zathura](https://pwmt.org/projects/zathura/) | PDF viewer with dark recolor and automatic tab-grouping |
| **Display Profiles** | [hyprmoncfg](https://github.com/crmne/hyprmoncfg) | Multi-monitor layout switcher and daemon |
| **Notifications** | [Dunst](https://dunst-project.org/) | Lightweight notification daemon |
| **Screen Lock / Idle** | [hyprlock](https://github.com/hyprwm/hyprlock) / [hypridle](https://github.com/hyprwm/hypridle) | Wayland screen locker and idle management |

---

## 🚀 Installation & Bootstrap

### 1. One-Line Bootstrap (Fresh Install)

To bootstrap a new machine with chezmoi:

```bash
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply dog42
```

### 2. Manual Clone & Apply

Alternatively, initialize and apply manually:

```bash
# Initialize chezmoi with git repository
chezmoi init git@github.com:dog42/dotfiles.git

# Review pending changes
chezmoi diff

# Apply dotfiles to user home directory
chezmoi apply
```

### Automated Setup Scripts

Chezmoi automatically executes the following provisioning scripts during bootstrap:
1. `run_once_before_00.sh.tmpl`: Unattended installation of Oh-My-Zsh.
2. `run_onchange_before_pkg.sh.tmpl`: Automated installation of official and AUR packages via `pacman` and `yay`.
3. `run_once_after_Z0.sh.tmpl`: Standalone IWD Wi-Fi network configuration, PlatformIO CLI, and Tailscale setup.
4. `run_onchange_after_reload-theme.sh.tmpl`: Automatically triggers desktop theme reload whenever `theme-colors.toml` changes.

---

## ⌨ Core Keybindings

A searchable list of all system and application keybindings is accessible via `SUPER + B`.

### Window & Workspace Management

| Shortcut | Description |
| :--- | :--- |
| `SUPER + Space` | Open application launcher (Walker) |
| `SUPER + Return` | Open terminal (Kitty) |
| `SUPER + SHIFT + C` | Close active window |
| `SUPER + SHIFT + E` | Logout / power options (hyprshutdown) |
| `SUPER + L` | Lock screen (hyprlock) |
| `SUPER + V` | Toggle floating mode for active window |
| `SUPER + Arrow Keys` | Move focus in direction |
| `SUPER + 1..9` | Switch to workspace 1..9 |
| `SUPER + SHIFT + 1..9` | Move active window to workspace 1..9 |
| `SUPER + R` | Reload Hyprland and Waybar |

### Window Grouping (Tabs)

| Shortcut | Description |
| :--- | :--- |
| `SUPER + W` | Toggle window group / tab container |
| `SUPER + Tab` | Next tab in group |
| `SUPER + SHIFT + Tab` | Previous tab in group |
| `SUPER + SHIFT + W` | Move window out of group (detach tab) |
| `SUPER + ALT + Arrow Keys` | Merge window into neighboring group |
| `SUPER + ,` / `SUPER + .` | Reorder tab left / right within groupbar |

### Applications & Tools

| Shortcut | Description |
| :--- | :--- |
| `SUPER + B` | Show context-aware keybinding cheatsheet (`showkeybindings`) |
| `SUPER + N` | Open text editor (Neovim) |
| `SUPER + Y` | Open terminal file manager (Yazi) |
| `SUPER + S` | Launch LocalSend |
| `SUPER + T` | Open Tailscale VPN menu in Walker |
| `SUPER + M` | Open monitor profile manager (hyprmoncfg) |
| `SHIFT + Print` | Capture screenshot of active window |
| `CTRL + Print` | Capture screenshot of selected region |
| `Print` | Capture screenshot of active monitor |

---

## 🎨 Centralized Theming

All UI component colors are derived from a single source of truth located at:

```text
.chezmoidata/theme-colors.toml
```

### Color Palette Overview

* **Backgrounds:** Pure OLED black (`#000000`), dark card surface (`#161616`), panel background (`#212121`).
* **Foregrounds:** Ash white primary text (`#e5e5e5`), muted subtitles (`#a7a7a7`), dim hints (`#686868`).
* **Accents:** Ember red (`#cc1111`), glowing scarlet (`#e54228`), alert red (`#ff2a2a`).
* **Status:** Moss green success (`#629c7d`), amber warnings (`#e49a44`), crimson errors (`#c53030`).

### Modifying Colors

1. Edit `.chezmoidata/theme-colors.toml` (or the root symlink `theme-colors.toml`).
2. Run `chezmoi apply`.
3. The script `run_onchange_after_reload-theme.sh.tmpl` automatically detects hash changes and refreshes Hyprland borders, Dunst notifications, Walker styles, and Waybar.

---

## 📁 Repository Structure

```text
├── .chezmoidata/
│   └── theme-colors.toml             # Central theme palette definition
├── dot_config/
│   ├── cheatsheets/                  # Plain-text cheatsheets (nvim, yazi, zathura, vimtricks)
│   ├── dunst/                        # Notification daemon configuration & templates
│   ├── fontconfig/                   # Monospace font aliases (JetBrainsMono Nerd Font)
│   ├── gtk-3.0/ & gtk-4.0/           # Dark GTK application preferences
│   ├── hypr/                         # Modular Hyprland Lua configuration
│   ├── hyprmoncfg/                   # Multi-monitor display profiles
│   ├── kitty/                        # Kitty terminal styling & theme templates
│   ├── nvim/                         # Neovim configuration (LazyVim base)
│   ├── walker/                       # Walker launcher configuration & stylesheet
│   ├── waybar/                       # Status bar layout, style & Tailscale scripts
│   ├── xkb/symbols/                  # Custom XKB keyboard layouts (gb_umlauts, us_umlauts)
│   ├── xournalpp/                    # Handwritten note-taking setup & Ashen palette
│   ├── yazi/                         # Yazi configuration, flavor & wayclip plugin
│   └── zathura/                      # PDF viewer settings & color templates
├── dot_local/share/bin/
│   ├── executable_chezmoi_do_update  # Interactive update helper
│   ├── executable_showkeybindings    # Context-aware keybindings viewer
│   └── executable_waybar-group-tabs  # Waybar tabbed-window management daemon
├── dot_bash_aliases                  # Shell aliases and Tailscale funnel QR utility (tsqr)
├── dot_zshrc                         # Zsh configuration & plugins
├── run_once_before_00.sh.tmpl        # Oh-My-Zsh unattended setup
├── run_onchange_before_pkg.sh.tmpl   # System & AUR package provisioning
└── run_once_after_Z0.sh.tmpl         # Network, compiler, and service bootstrapping
```

---

## 💡 Post-Install Tips & Addons

### Git SSH / HTTPS Rewrites

Configure Git to push over SSH while pulling over HTTPS:

```bash
git config --global url."https://github.com/".insteadOf git@github.com:
git config --global url."git@github.com:".pushInsteadOf https://github.com/
```

### LaTeX & VimTeX Setup

For compiling LaTeX documents with LuaLaTeX and live Zathura preview:

```bash
# Install TeX Live (Zathura is automatically installed during bootstrap)
sudo pacman -S texlive-meta

# Add the following magic comment to the first line of your .tex file to enforce LuaLaTeX:
# %! TeX program = lualatex
```

### LocalSend Firewall Rules

If using `ufw`, open the default ports for LocalSend file transfer:

```bash
sudo ufw allow 53317/tcp
sudo ufw allow 53317/udp
```

### Updating Dotfiles

Check for updates from the remote repository and apply changes:

```bash
chezmoi update
# Or use the interactive update helper:
chezmoi_do_update
```
