local lspkind = require('lspkind')
local cmp = require('cmp')

cmp.setup({
  formatting = {
    format = lspkind.cmp_format({
      mode = 'symbol_text', -- Show only symbol annotations.
      maxwidth = 50, -- Prevent the popup from showing more than provided characters (e.g 50 will not show more than 50 characters).
      ellipsis_char = '...', -- When popup menu exceed maxwidth, the truncated part would show ellipsis_char instead (must define maxwidth first).
      preset = 'default',
      menu = ({
        buffer = '[Buffer]',
        nvim_lsp = '[LSP]',
      }),
    })
  },
})
