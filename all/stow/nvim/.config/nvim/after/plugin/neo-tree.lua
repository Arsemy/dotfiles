require('neo-tree').setup({
  popup_border_style = 'single',
  enable_diagnostics = false,
  close_if_last_window = true,
  window = {
    position = 'left',
    width = 32,
  },
  filesystem = {
    follow_current_file = true,
  },
})

vim.cmd('let g:neo_tree_remove_legacy_commands = 1')

vim.keymap.set('n', '<leader>nt', '<CMD>NeoTreeShowToggle<CR>')
