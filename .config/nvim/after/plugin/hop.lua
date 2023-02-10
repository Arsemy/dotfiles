require('hop').setup({
  keys = 'etovxqpdygfblzhckisuran'
})

-- Place this in one of your configuration file(s).
local hop = require('hop')
local directions = require('hop.hint').HintDirection

vim.keymap.set('', '<leader>a', function()
  hop.hint_words()
end)
vim.keymap.set('', '<leader>l', function()
  hop.hint_lines_skip_whitespace()
end)
vim.keymap.set('', '<leader>L', function()
  hop.hint_lines()
end)
vim.keymap.set('', 'f', function()
  hop.hint_char1({ direction = directions.AFTER_CURSOR, current_line_only = true, case_insensitive = false })
end, {remap = true})
vim.keymap.set('', 'F', function()
  hop.hint_char1({ direction = directions.BEFORE_CURSOR, current_line_only = true, case_insensitive = false })
end, {remap = true})
