# SETUPPC

## set keymap and umlaute

  sudo nvim /usr/share/X11/xkb/symbols/gb-umlauts

    artial alphanumeric_keys
    xkb_symbols "custom_uml" {

        include "gb(basic)"
    
        name[Group1]= "UK with Umlauts";
    
        key <AC01> { [ a, A, adiaeresis, Adiaeresis ] }; // A key
        key <AD09> { [ o, O, odiaeresis, Odiaeresis ] }; // O key
        key <AD07> { [ u, U, udiaeresis, Udiaeresis ] }; // U key
        key <AC02> { [ s, S, ssharp, section ] };        // S key
    
        key <AD03> { [ e, E, EuroSign, cent ] };         // E key
    };

  nvim .config/hypr/input.conf
  
    kb_layout = gb-umlauts
    kb_variant = custom_uml

  reload hyperland

## ✅ conf keybindings

  add to .config/hypr/bindings.conf

    bind=SUPER CTRL,left,resizeactive,-10 0
    bind=SUPER CTRL,right,resizeactive,10 0
    bind=SUPER CTRL,up,resizeactive,0 -10
    bind=SUPER CTRL,down,resizeactive,0 10
    
    unbind = SUPER SHIFT, C
    bind = SUPER SHIFT, C, killactive
    unbind = SUPER, F
    bindd = SUPER, F, File manager, exec, $terminal -e yazi

  remove

    #bindd = SUPER, F, File manager, exec, uwsm app -- nautilus --new-window
    unbind = SUPER, W 

## ✅ conf monitor

  nvim .config/hypr/monitors.conf

    env = GDK_SCALE,1
    monitor=,preferred,auto,1.666667

## conf hyperland

  nvim .config/hypr/looknfeel.conf

  omarchy-theme-install <https://github.com/bjarneo/omarchy-nes-theme>

## conf waybar

  nvim .config/waybar/config.jsonc
  
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

  omarchy-restart-waybar

## install kitty as treminal

  omarchy-install-terminal kitty

  kitten themes

## install zsh and ohmyzsh
  
  sudo pacman -S zsh

  sh -c "$(curl -fsSL <https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh>)" "" --unattended

  chsh -s /usr/bin/zsh

  echo -e '\nshell /usr/bin/zsh\n' >> ~/.config/kitty/kitty.conf

## install yazi as filemanager
  
  sudo pacman -S yazi

  ya pkg add ficd0/ashen:ashen

  echo -e '[flavor]\ndark = "ashen"' > ~/.config/yazi/theme.toml

## ✅ install nvim conf

  mv ~/.config/nvim/ ~/.config/nvim.bak/

  git clone <https://gitlab.com/dog42/lazyvim.git> ~/.config/nvim

  (maybe install npm if pyright cant be installed)
