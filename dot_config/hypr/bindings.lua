-- See https://wiki.hypr.land/Configuring/Keywords/

-- Example binds, see https://wiki.hypr.land/Configuring/Binds/ for more
hl.bind("SUPER + return", hl.dsp.exec_cmd(terminal), { description = "terminal" })
hl.bind("SUPER + SHIFT + C", hl.dsp.window.close(), { description = "killactive" })
hl.bind("SUPER + SHIFT + E", hl.dsp.exec_cmd("command -v hyprshutdown >/dev/null 2>&1 && hyprshutdown || hyprctl dispatch exit"), { description = "logout" })
hl.bind("SUPER + R", hl.dsp.exec_cmd("hyprctl reload & killall -SIGUSR2 waybar"), { description = "reload hypr and waybar" })
hl.bind("SUPER + L", hl.dsp.exec_cmd("hyprlock"), { description = "lock screen" })
hl.bind("SUPER + Y", hl.dsp.exec_cmd(terminal .. " -e yazi"), { description = "file manager" })
hl.bind("SUPER + N", hl.dsp.exec_cmd(terminal .. " -e nvim"), { description = "editor/nvim" })
hl.bind("SUPER + S", hl.dsp.exec_cmd("localsend"), { description = "localsend" })
hl.bind("SUPER + V", hl.dsp.window.float({ action = "toggle" }), { description = "toggle floating window" })
hl.bind("SUPER + space", hl.dsp.exec_cmd(menu), { description = "launcher" })
hl.bind("SUPER + B", hl.dsp.exec_cmd("showkeybindings"), { description = "show keybindings" })
hl.bind("SUPER + M", hl.dsp.exec_cmd(terminal .. " -e hyprdynamicmonitors tui"), { description = "monitorconfig" })
hl.bind("SUPER + T", hl.dsp.exec_cmd((os.getenv("HOME") or "") .. "/.config/waybar/waybar-tailscale/waybar-tailscale.sh --menue"), { description = "tailscale-waybar-menue" })
hl.bind("SUPER + G", hl.dsp.exec_cmd("type agy && " .. terminal .. " -e agy || antigravity-ide"), { description = "gemeni/antigravity-cli" })

-- Screenshot
hl.bind("SHIFT + PRINT", hl.dsp.exec_cmd("hyprshot -m window -o " .. (os.getenv("HOME") or "") .. "/Bilder/screenshot"), { description = "Screenshot" })
hl.bind("CTRL + PRINT", hl.dsp.exec_cmd("hyprshot -m region -o " .. (os.getenv("HOME") or "") .. "/Bilder/screenshot"), { description = "Screenshot" })
hl.bind("PRINT", hl.dsp.exec_cmd("hyprshot -m output -m active -o " .. (os.getenv("HOME") or "") .. "/Bilder/screenshot"), { description = "Screenshot" })

-- Move focus with mainMod + arrow keys
hl.bind("SUPER + left", hl.dsp.focus({ direction = "l" }), { description = "Move focus with mainMod + arrow keys" })
hl.bind("SUPER + right", hl.dsp.focus({ direction = "r" }), { description = "Move focus with mainMod + arrow keys" })
hl.bind("SUPER + up", hl.dsp.focus({ direction = "u" }), { description = "Move focus with mainMod + arrow keys" })
hl.bind("SUPER + down", hl.dsp.focus({ direction = "d" }), { description = "Move focus with mainMod + arrow keys" })

-- Switch workspaces with mainMod + [0-9]
-- Move active window to a workspace with mainMod + SHIFT + [0-9]
for i = 1, 10 do
    local key = i % 10 -- 10 maps to key 0
    hl.bind("SUPER + " .. key,                         hl.dsp.focus({ workspace = i}), { description = "Switch workspaces with mainMod + [0-9]" })
    hl.bind("SUPER + SHIFT + " .. key,         hl.dsp.window.move({ workspace = i, follow = false }), { description = "Move active window to a workspace with mainMod + SHIFT + [0-9]" })
end

-- resize window
hl.bind("SUPER + CTRL + left", hl.dsp.window.resize({ x = -20, y = 0, relative = true }), { repeating = true , description = "resize window" })
hl.bind("SUPER + CTRL + right", hl.dsp.window.resize({ x = 20, y = 0, relative = true }), { repeating = true , description = "resize window" })
hl.bind("SUPER + CTRL + up", hl.dsp.window.resize({ x = 0, y = -20, relative = true }), { repeating = true , description = "resize window" })
hl.bind("SUPER + CTRL + down", hl.dsp.window.resize({ x = 0, y = 20, relative = true }), { repeating = true , description = "resize window" })

-- move window to other monitor
hl.bind("SUPER + SHIFT + left", hl.dsp.window.move({ direction = "l" }), { description = "move window to other monitor" })
hl.bind("SUPER + SHIFT + right", hl.dsp.window.move({ direction = "r" }), { description = "move window to other monitor" })
hl.bind("SUPER + SHIFT + up", hl.dsp.window.move({ direction = "u" }), { description = "move window to other monitor" })
hl.bind("SUPER + SHIFT + down", hl.dsp.window.move({ direction = "d" }), { description = "move window to other monitor" })

-- Scroll through existing workspaces with mainMod + scroll
hl.bind("SUPER + mouse_down", hl.dsp.focus({ workspace = "e+1" }), { description = "Scroll through existing workspaces with mainMod + scroll" })
hl.bind("SUPER + mouse_up", hl.dsp.focus({ workspace = "e-1" }), { description = "Scroll through existing workspaces with mainMod + scroll" })

-- Move/resize windows with mainMod + LMB/RMB and dragging
hl.bind("SUPER + mouse:272", hl.dsp.window.drag(), { mouse = true , description = "Move/resize windows with mainMod + LMB/RMB and dragging" })
hl.bind("SUPER + mouse:273", hl.dsp.window.resize(), { mouse = true , description = "Move/resize windows with mainMod + LMB/RMB and dragging" })

-- Laptop multimedia keys for volume and LCD brightness
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"), { repeating = true, locked = true , description = "Laptop multimedia keys for volume and LCD brightness" })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"), { repeating = true, locked = true , description = "Laptop multimedia keys for volume and LCD brightness" })
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), { repeating = true, locked = true , description = "Laptop multimedia keys for volume and LCD brightness" })
hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"), { repeating = true, locked = true , description = "Laptop multimedia keys for volume and LCD brightness" })
hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%+"), { repeating = true, locked = true , description = "Laptop multimedia keys for volume and LCD brightness" })
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%-"), { repeating = true, locked = true , description = "Laptop multimedia keys for volume and LCD brightness" })

-- Requires playerctl
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"), { locked = true , description = "Requires playerctl" })
hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true , description = "Requires playerctl" })
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true , description = "Requires playerctl" })
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"), { locked = true , description = "Requires playerctl" })
