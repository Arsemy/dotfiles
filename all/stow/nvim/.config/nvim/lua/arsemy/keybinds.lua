-- Shorten for 'vim.keymap.set'.
local function map(mode, key, cmd, ...)
  vim.keymap.set(mode, key, cmd, { silent = true, ... })
end

-- Leader key.
map('', '<space>', '<nop>')
map('', '<c-space>', '<nop>')
vim.g.mapleader = ' '

-- Copy to system clipboard.
map({'n', 'x'}, '<leader>y', '"+y')

-- Paste on selected and don't copy to clipboard.
map('x', '<leader>p', '\"_dP')

-- Delete and don't copy to clipboard.
map({'n', 'x'}, '<leader>d', '\"_d')

-- Wrap text toggle
map('n', '<leader>w', '<cmd>set wrap!<cr>')

-- Clear '/' characters match finder.
map('n', '<leader>nn', '<cmd>noh<cr>')

-- Relative numbers toggle.
map('n', '<leader>rl', '<cmd>setlocal relativenumber!<cr>')

-- Remove trailing whitespace
map('n', '<leader>tr', '<cmd>lua trimWhiteSpace()<cr>')

-- Move to the next/previous buffer.
map('n', '<leader>[', '<cmd>bp<cr>')
map('n', '<leader>]', '<cmd>bn<cr>')

-- Cursor go to middle on half page movement.
map('n', '<c-d>', '<C-d>zz')
map('n', '<c-u>', '<C-u>zz')

-- Find and keep the cursor in the middle.
map('n', 'n', 'nzzzv')
map('n', 'N', 'Nzzzv')

-- Change window focus
map('n', '<c-h>', '<c-w>h')
map('n', '<c-j>', '<c-w>j')
map('n', '<c-k>', '<c-w>k')
map('n', '<c-l>', '<c-w>l')

-- Resize windows with arrows.
map('n', '<a-k>', '<cmd>resize +2<cr>')
map('n', '<a-j>', '<cmd>resize -2<cr>')
map('n', '<a-h>', '<cmd>vertical resize -2<cr>')
map('n', '<a-l>', '<cmd>vertical resize +2<cr>')
