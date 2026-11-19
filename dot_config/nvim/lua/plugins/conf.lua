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
  -- { "normen/vim-pio" },
  -- { "skywind3000/asyncrun.vim" }, -- async compile/make for platformio

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
  {
    "lervag/vimtex",
    lazy = false, -- VimTeX must be loaded on startup for .tex files
    init = function()
      -- 1. Set PDF viewer to Zathura
      vim.g.vimtex_view_method = "zathura"

      -- 2. Switch compiler to LuaLaTeX
      vim.g.vimtex_compiler_method = "latexmk"
      vim.g.vimtex_compiler_latexmk = {
        executable = "latexmk",
        options = {
          "-shell-escape",
          "-verbose",
          "-file-line-error",
          "-synctex=1",
          "-interaction=nonstopmode",
          "-lualatex", -- Hier erzwingen wir LuaLaTeX
        },
      }

      -- Set PDF mode to 4 (LuaLaTeX)
      vim.g.vimtex_compiler_latexmk = vim.tbl_extend("force", vim.g.vimtex_compiler_latexmk, {
        pdf_mode = 4, -- 4 corresponds to LuaLaTeX
      })

      -- 3. Automatically open viewer after first compilation
      vim.g.vimtex_view_forward_search_on_start = true
      -- 4. ignore some warnings
      vim.g.vimtex_quickfix_ignore_filters = {
        "Overfull",
        "Underfull",
      }
    end,
  },
}
