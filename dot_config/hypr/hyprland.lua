-- Global Variables
shell = "/bin/zsh"
terminal = "kitty"
fileManager = "yazi"
editor = "nvim"
menu = "walker"

-- Load modules
require("monitors")
require("input")
require("bindings")
require("looknfeel")
require("envs")
require("autostart")
require("workspaces")

-- Window Rules
hl.window_rule({ suppress_event = "maximize", match = { class = ".*" } })

-- Fix some dragging issues with XWayland
hl.window_rule({
	no_focus = true,
	match = {
		class = "^$",
		title = "^$",
		xwayland = true,
		float = true,
		fullscreen = false,
		pin = false,
	},
})

-- Hyprland-run windowrule
hl.window_rule({
	move = "20 monitor_h-120",
	float = true,
	match = { class = "hyprland-run" },
})

hl.config({
	input = {
		touchdevice = {
			output = "eDP-1", -- Replace $monitor0 with your desired monitor (e.g., $monitor1, HDMI-A-1)
			transform = 0, -- Adjust if needed for rotation
		},
		tablet = {
			output = "eDP-1", -- Applies to pen input if used
			transform = 0,
		},
	},
	xwayland = {
		force_zero_scaling = true,
	},
})
