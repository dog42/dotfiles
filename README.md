# SETUPPC - TODO

## Info

It's a good idea to configure Git to use SSH for pushing (uploading) and HTTPS for pulling (downloading), use Git's insteadOf and pushInsteadOf configuration options.

```git config --global url."https://github.com/".insteadOf git@github.com:```

```git config --global url."git@github.com:".pushInsteadOf https://github.com/```

## Latex and vimtex (\ll)

install TexLive

`sudo pacman -S texlive-meta`

install TexLive "Full"

`sudo pacman -S texlive-basic texlive-latexextra texlive-fontsrecommended texlive-fontsextra texlive-langgerman texlive-luatex texlive-bibtexextra texlive-pictures`

install zathura for pdf preview ()

`sudo pacman -S zathura zathura-pdf-poppler`

add magic comment to .tex file to force lualatex

`%! TeX program = lualatex`

## ❌ allow "localsend" in firewall

```sudo ufw allow 53317/tcp```

```sudo ufw allow 53317/udp```

## ❓ install zsh and ohmyzsh

  ❓ first install, then move '.oh-my-zsh'-folder
  
  ```sudo pacman -S zsh```

  ```sh -c "$(curl -fsSL <https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh>)" "" --unattended```

  ```chsh -s /usr/bin/zsh```

  ```echo -e '\nshell /usr/bin/zsh\n' >> ~/.config/kitty/kitty.conf```

## ✅ set keymap and umlaute

  ```sudo nvim /usr/share/X11/xkb/symbols/gb-umlauts```

    partial alphanumeric_keys
    xkb_symbols "basic" {

        include "gb"
        name[Group1]= "UK with Umlauts";

        include "level3(ralt_switch)"

        key <AC01> { [ a, A, adiaeresis, Adiaeresis ] };
        key <AD09> { [ o, O, odiaeresis, Odiaeresis ] };
        key <AD07> { [ u, U, udiaeresis, Udiaeresis ] };
        key <AC02> { [ s, S, ssharp,     section    ] };
        key <AD03> { [ e, E, EuroSign,   cent       ] };
    };

```nvim .config/hypr/input.conf```
  
    kb_layout = gb-umlauts
    kb_variant = custom_uml

  reload hyperland

## ✅ conf waybar

  ```nvim .config/waybar/config.jsonc```
  
    "battery#0","battery#1"


    "battery#0": {
      "bat": "BAT0",
      "format": "{icon}",
      "format-discharging": "{icon}",
      "format-charging": "{icon}",
      "format-plugged": "",
      "format-icons": {
        "charging": ["󰢜", "󰂆", "󰂇", "󰂈", "󰢝", "󰂉", "󰢞", "󰂊", "󰂋", "󰂅"],
        "default": ["󰁺", "󰁻", "󰁼", "󰁽", "󰁾", "󰁿", "󰂀", "󰂁", "󰂂", "󰁹"]
      },
      "format-full": "󰂅",
      "tooltip-format": "INT {capacity}%",
      "tooltip-format-discharging": "INT {power:>1.0f}W↓ {capacity}%",
      "tooltip-format-charging": "INT {power:>1.0f}W↑ {capacity}%",
      "interval": 5,
      "on-click": "omarchy-menu power",
      "states": {
        "warning": 20,
        "critical": 10
      }
    },
    "battery#1": {
      "bat": "BAT1",
      "format": "{icon}",
      "format-discharging": "{icon}",
      "format-charging": "{icon}",
      "format-plugged": "",
      "format-icons": {
        "charging": ["󰢜", "󰂆", "󰂇", "󰂈", "󰢝", "󰂉", "󰢞", "󰂊", "󰂋", "󰂅"],
        "default": ["󰁺", "󰁻", "󰁼", "󰁽", "󰁾", "󰁿", "󰂀", "󰂁", "󰂂", "󰁹"]
      },
      "format-full": "󰂅",
      "tooltip-format": "EXT {capacity}%",
      "tooltip-format-discharging": "EXT {power:>1.0f}W↓ {capacity}%",
      "tooltip-format-charging": "EXT {power:>1.0f}W↑ {capacity}%",
      "interval": 5,
      "on-click": "omarchy-menu power",
      "states": {
        "warning": 20,
        "critical": 10
      }
    },
