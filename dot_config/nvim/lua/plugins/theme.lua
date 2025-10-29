return {
  -- load colorscheme
  -- { "catppuccin/nvim", name = "catppuccin", priority = 1000 },
  -- { "ellisonleao/gruvbox.nvim" },
  {
    "ficcdaf/ashen.nvim",
    opts = {
      colors = {
        background = "#000000",
        -- standard red colors
        red_glowing = "#991111", -- Slightly deeper glowing red "#DF6464"
        red_ember = "#cc1111", -- Deep, smoldering ember red "#B14242"
      },
      hl = {
        merge_override = {
          CursorLineNr = { "red_ember", "g_9" },
          LineNr = { "g_7", "background" },
        },
      },
    },
  },
  -- Configure LazyVim to load colorscheme
  {
    "LazyVim/LazyVim",
    opts = {
      -- colorscheme = "catppuccin" ,
      -- colorscheme = "gruvbox",
      colorscheme = "ashen",
      -- underline = false,
    },
  },
  {
    "folke/snacks.nvim",
    opts = {
      dashboard = {
        sections = {
          { section = "header" },
          { section = "keys", gap = 0, padding = 1 },
          { icon = " ", title = "Recent Files", section = "recent_files", limit = 3, indent = 2, padding = 1 },
          -- { section = "startup" },
        },
        preset = {
          header = [[
                                  |\_/|                                               
                                  | 0 0                                               
                                  |   <>              _                               
                                  |  _/\------____   | |                              
                                  |               `--' |                              
                              ____|_       ___|   |___.'                              
                             /_/_____/____/_______|                                   
            ██╗      █████╗ ███████╗██╗   ██╗██████╗  ██████╗  ██████╗              
            ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔════╝              
            ██║     ███████║  ███╔╝  ╚████╔╝ ██║  ██║██║   ██║██║  ███╗             
            ██║     ██╔══██║ ███╔╝    ╚██╔╝  ██║  ██║██║   ██║██║   ██║             
            ███████╗██║  ██║███████╗   ██║   ██████╔╝╚██████╔╝╚██████╔╝             
            ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝  ╚═════╝  ╚═════╝              
         ]],
        },
      },
    },
  },

  {
    "nvim-lualine/lualine.nvim",
    opts = {
      sections = {
        lualine_z = {
          {
            "filename",
            symbols = {
              modified = " +++UNSAVED+++",
            },
          },
        },
      },
    },
  },
}
