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

-- Window splits and close
vim.keymap.set("n", "<leader>wv", "<C-w>v", { desc = "Split vertical" })
vim.keymap.set("n", "<leader>wh", "<C-w>s", { desc = "Split horizontal" })
vim.keymap.set("n", "<leader>we", "<C-w>=", { desc = "Balance window splits" })
vim.keymap.set("n", "<leader>wx", "<cmd>close<CR>", { desc = "Close window split" })
vim.keymap.set("n", "<leader>wq", "<cmd>close<CR>", { desc = "Close window split" })

-- Window navigation with Space + w + arrow keys
vim.keymap.set("n", "<Leader>w<Left>", "<C-w>h", { desc = "Focus window left" })
vim.keymap.set("n", "<Leader>w<Down>", "<C-w>j", { desc = "Focus window down" })
vim.keymap.set("n", "<Leader>w<Up>", "<C-w>k", { desc = "Focus window up" })
vim.keymap.set("n", "<Leader>w<Right>", "<C-w>l", { desc = "Focus window right" })

-- Directional navigation (h, j, k, l)
vim.keymap.set("n", "<Leader>wh", "<C-w>h", { desc = "Focus window left" })
vim.keymap.set("n", "<Leader>wj", "<C-w>j", { desc = "Focus window down" })
vim.keymap.set("n", "<Leader>wk", "<C-w>k", { desc = "Focus window up" })
vim.keymap.set("n", "<Leader>wl", "<C-w>l", { desc = "Focus window right" })

-- Generic window cycling with Space + w + w
vim.keymap.set("n", "<Leader>ww", "<C-w>w", { desc = "Next window" })

-- Spelling correction suggestions on 'zz' (uses LazyVim vim.ui.select popup)
vim.keymap.set("n", "zz", function()
  local badword = vim.fn.spellbadword()[1]
  local word = badword ~= "" and badword or vim.fn.expand("<cword>")
  if word == "" then
    return
  end
  local suggestions = vim.fn.spellsuggest(word)
  if #suggestions == 0 then
    vim.notify("No suggestions found for '" .. word .. "'", vim.log.levels.INFO)
    return
  end
  vim.ui.select(suggestions, {
    prompt = "Spelling suggestions for '" .. word .. "':",
  }, function(selected, idx)
    if selected and idx then
      vim.cmd("normal! " .. idx .. "z=")
    end
  end)
end, { desc = "Spelling suggestions (popup)" })

-- Toggle Neo-tree with TAB
vim.keymap.set("n", "<Tab>", function()
  require("neo-tree.command").execute({ toggle = true, dir = LazyVim.root() })
end, { desc = "Toggle Neo-tree" })
