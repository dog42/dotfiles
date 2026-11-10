return {
  "folke/which-key.nvim",
  -- event = "VeryLazy",
  -- opts = {
  --   -- your configuration comes here
  --   -- or leave it empty to use the default settings
  --   -- refer to the configuration section below
  -- },
  keys = {
    {
      "\\h",
      function()
        print("Hello YOU")
      end,
      desc = "Hello from (which-key)",
    },
  },
}
