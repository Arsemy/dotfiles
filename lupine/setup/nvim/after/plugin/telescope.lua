require('telescope').setup({
  defaults = {
    prompt_prefix = '  ',
    borderchars = { '─', '│', '─', '│', '┌', '┐', '┘', '└' }
  },
  extensions = {
    undo = {
      initial_mode = 'normal',
      scroll_strategy = 'limit',
      side_by_side = true,
      layout_strategy = 'horizontal',
      use_delta = true,
      use_custom_command = nil, -- setting this implies `use_delta = false`. Accepted format is: { "bash", "-c", "echo '$DIFF' | delta" }
      diff_context_lines = vim.o.scrolloff,
      entry_format = "state #$ID, $STAT, $TIME",
      mappings = {
        n = {
          ["<cr>"] = require("telescope-undo.actions").restore,
          ["ya"] = require("telescope-undo.actions").yank_additions,
          ["yd"] = require("telescope-undo.actions").yank_deletions,
        },
      },
    },
  },
})

local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files)
vim.keymap.set('n', '<leader>fg', builtin.live_grep)
vim.keymap.set('n', '<leader>fb', builtin.buffers)
vim.keymap.set('n', '<leader>fh', builtin.help_tags)
vim.keymap.set('n', '<leader>fd', '<cmd>Telescope diagnostics initial_mode=normal<cr>')

require('telescope').load_extension('undo')
vim.keymap.set('n', '<leader>u', '<cmd>Telescope undo<cr>')
