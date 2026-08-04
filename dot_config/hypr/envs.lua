-- See https://wiki.hypr.land/Configuring/Environment-variables/

hl.env("XCURSOR_SIZE", "24")
hl.env("HYPRCURSOR_SIZE", "24")
hl.env("TERMINAL", terminal)
hl.env("EDITOR", editor)
hl.env("SHELL", shell)
hl.env("PATH", (os.getenv("PATH") or "") .. ":" .. (os.getenv("HOME") or "") .. "/.local/share/bin:" .. (os.getenv("HOME") or "") .. "/.local/bin")
hl.env("TERM", "xterm-color")
