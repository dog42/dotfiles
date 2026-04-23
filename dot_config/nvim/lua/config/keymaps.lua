-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
-- vim.keymap.set({ "i", "x", "n", "s" }, "<C-s>", "<cmd>w<cr><esc>", { desc = "Save File" })
-- vim.keymap.set("n", "<leader>mm", ":w<CR>:copen<CR><ESC>:AsyncRun make<CR>", { desc = "run make async" })
-- vim.keymap.set("n", "<leader>mu", ":w<CR>:copen<CR><ESC>:AsyncRun make upload<CR>", { desc = "run make upload async" })
-- vim.keymap.set("n", "<leader>mc", ":copen<CR><ESC>:PIOMonitor<CR>", { desc = "run PIOMonitor" })
vim.keymap.set("n", "<S-Left>", "<cmd>bprevious<cr>", { desc = "Prev Buffer" })
vim.keymap.set("n", "<S-Right>", "<cmd>bnext<cr>", { desc = "Next Buffer" })
-- vim.keymap.set("n", "<cr>", "za", { desc = "toggle fold" })
vim.keymap.set("n", "<leader>h", Snacks.dashboard.open, { desc = "Dashboard/Open mini starter" })

-- Fensterwechsel mit Space + w + Pfeiltasten
vim.keymap.set("n", "<Leader>w<Left>", "<C-w>h", { desc = "Fenster links" })
vim.keymap.set("n", "<Leader>w<Down>", "<C-w>j", { desc = "Fenster unten" })
vim.keymap.set("n", "<Leader>w<Up>", "<C-w>k", { desc = "Fenster oben" })
vim.keymap.set("n", "<Leader>w<Right>", "<C-w>l", { desc = "Fenster rechts" })

-- Zusätzlich die Buchstaben-Variante (h,j,k,l) - falls du sie mal brauchst
vim.keymap.set("n", "<Leader>wh", "<C-w>h", { desc = "Fenster links" })
vim.keymap.set("n", "<Leader>wj", "<C-w>j", { desc = "Fenster unten" })
vim.keymap.set("n", "<Leader>wk", "<C-w>k", { desc = "Fenster oben" })
vim.keymap.set("n", "<Leader>wl", "<C-w>l", { desc = "Fenster rechts" })

-- Das generische Wechseln mit Space + w + w
vim.keymap.set("n", "<Leader>ww", "<C-w>w", { desc = "Nächstes Fenster" })
