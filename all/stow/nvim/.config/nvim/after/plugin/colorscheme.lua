require('tokyonight').setup({
  style = 'night', -- The theme comes in three styles, `storm`, `moon`, a darker variant `night` and `day`.
  transparent = true, -- Enable this to disable setting the background color.
  terminal_colors = true, -- Configure the colors used when opening a `:terminal` in Neovim.
  styles = {
    -- Background styles. Can be "dark", "transparent" or "normal".
    sidebars = 'transparent', -- Style for sidebars, see below.
    floats = 'transparent', -- Style for floating windows.
  },
  lualine_bold = true, -- When `true`, section headers in the lualine theme will be bold.
})

vim.cmd('colorscheme tokyonight')
vim.cmd('hi LineNr guibg=none guifg=#a9b1d6')
vim.cmd('hi ColorColumn ctermbg=0 guibg=#16161e')
vim.cmd('hi FloatBorder guifg=#c0caf5')
vim.cmd('hi NormalFloat guifg=#c0caf5')
vim.cmd('hi TelescopeBorder guifg=#c0caf5')
vim.cmd('hi TelescopeNormal guifg=#c0caf5')
vim.cmd('hi Pmenu guibg=NONE')
