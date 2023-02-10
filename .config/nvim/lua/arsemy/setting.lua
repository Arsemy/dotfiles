vim.opt.termguicolors = true

vim.opt.nu = true
vim.opt.relativenumber = true

vim.opt.splitright = true

vim.opt.smartindent = true

vim.opt.wrap = false

vim.opt.swapfile = false
vim.opt.backup = false

-- Have files of undo history to use after reboot.
vim.opt.undofile = true
vim.opt.undodir = os.getenv('HOME') .. '/.local/share/nvim/undodir'

-- Search ('/') without focusing the first pattern.
vim.opt.incsearch = true

-- Width (measured in spaces) of a tab character.
vim.opt.tabstop = 4
-- Width (measured in spaces) of a indent. It's used by =, < and > commands.
vim.opt.shiftwidth = 4
vim.opt.softtabstop = 4
-- Insert spaces instead of tabs.
vim.opt.expandtab = true

-- Cursor centered vertically.
vim.opt.scrolloff = 8

-- Literally a column for signs.
vim.opt.signcolumn = 'yes'

-- Time to write to swap file or verify cursorhold events.
vim.opt.updatetime = 50
