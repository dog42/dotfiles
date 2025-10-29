if false then
  return {}
end

-- every spec file under the "plugins" directory will be loaded automatically by lazy.nvim
--
-- In your plugin files, you can:
-- * add extra plugins
-- * disable/enabled LazyVim plugins
-- * override the configuration of LazyVim plugins
return {

  -- older vim-Platformio-Plugin, old but good; https://github.com/normen/vim-pio
  { "normen/vim-pio" },
  { "skywind3000/asyncrun.vim" }, -- async compile/make for platformio

  -- newer nvim-Platformio-Plugin, but with some bugs; https://github.com/anurag3301/nvim-platformio.lua
  --{
  --  "anurag3301/nvim-platformio.lua",
  --  dependencies = {
  --    { "akinsho/nvim-toggleterm.lua" },
  --    { "nvim-telescope/telescope.nvim" },
  --    { "nvim-lua/plenary.nvim" },
  --  },
  --},

  -- add more treesitter parsers
  {
    "nvim-treesitter/nvim-treesitter",
    opts = {
      ensure_installed = {
        "c",
        "cpp",
        "bash",
        "html",
        "javascript",
        "json",
        "lua",
        "markdown",
        "markdown_inline",
        "vim",
        "yaml",
      },
    },
  },
}
