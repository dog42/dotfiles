-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
-- vim.keymap.set({ "i", "x", "n", "s" }, "<C-s>", "<cmd>w<cr><esc>", { desc = "Save File" })
vim.keymap.set("n", "<leader>mm", ":w<CR>:copen<CR><ESC>:AsyncRun make<CR>", { desc = "run make async" })
vim.keymap.set("n", "<leader>mu", ":w<CR>:copen<CR><ESC>:AsyncRun make upload<CR>", { desc = "run make upload async" })
vim.keymap.set("n", "<leader>mc", ":copen<CR><ESC>:PIOMonitor<CR>", { desc = "run PIOMonitor" })
vim.keymap.set("n", "<S-Left>", "<cmd>bprevious<cr>", { desc = "Prev Buffer" })
vim.keymap.set("n", "<S-Right>", "<cmd>bnext<cr>", { desc = "Next Buffer" })
-- vim.keymap.set("n", "<cr>", "za", { desc = "toggle fold" })
vim.keymap.set("n", "<leader>h", Snacks.dashboard.open, { desc = "Dashboard/Open mini starter" })
