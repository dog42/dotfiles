# SETUPPC - TODO
## Info

It's a good idea to configure Git to use SSH for pushing (uploading) and HTTPS for pulling (downloading), use Git's insteadOf and pushInsteadOf configuration options.

```git config --global url."https://github.com/".insteadOf git@github.com:```

```git config --global url."git@github.com:".pushInsteadOf https://github.com/```   

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
