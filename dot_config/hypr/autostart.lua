-- AUTOSTART

hl.on("hyprland.start", function()
    -- unlock kwallet
    hl.exec_cmd("sleep 0 && /usr/lib/pam_kwallet_init && sleep 1")
    
    hl.exec_cmd("hyprdynamicmonitors run")
    hl.exec_cmd("[workspace 2 silent] " .. terminal)
    hl.exec_cmd("hyprpaper")
    hl.exec_cmd("waybar")
    hl.exec_cmd("[workspace 1 silent] brave")
    hl.exec_cmd("walker --gapplication-service")
    hl.exec_cmd("elephant")
    hl.exec_cmd("dunst")
    hl.exec_cmd("hypridle")
    hl.exec_cmd("udiskie")
    hl.exec_cmd("seafile-applet")
end)
