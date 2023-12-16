local function lsp_highlight_document(client)
  if client.server_capabilities.documentHighlightProvider then
    vim.cmd [[
    hi! LspReferenceRead cterm=bold ctermbg=red guibg=#414868
    hi! LspReferenceText cterm=bold ctermbg=red guibg=#416852
    hi! LspReferenceWrite cterm=bold ctermbg=red guibg=#424f8a
    augroup lsp_document_highlight
    autocmd! * <buffer>
    autocmd! CursorHold <buffer> lua vim.lsp.buf.document_highlight()
    autocmd! CursorHoldI <buffer> lua vim.lsp.buf.document_highlight()
    autocmd! CursorMoved <buffer> lua vim.lsp.buf.clear_references()
    autocmd! CursorMovedI <buffer> lua vim.lsp.buf.clear_references()
    augroup END
    ]]
  end
end

local border = 'single'
local handlers =  {
  ["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, { border = border, }),
  ["textDocument/signatureHelp"] = vim.lsp.with(vim.lsp.handlers.signature_help, { border = border, }),
}

vim.diagnostic.config({
  virtual_text = false,
  float = { border=border, prefix=' ', source='always', },
  update_in_insert = true,
  underline = true,
})

local on_attach = function(client, bufnr)
  vim.cmd [[
  highlight! DiagnosticLineNrError guifg=#f7768e gui=bold
  highlight! DiagnosticLineNrWarn guifg=#e0af68 gui=bold
  highlight! DiagnosticLineNrInfo guifg=#7dcfff gui=bold
  highlight! DiagnosticLineNrHint guifg=#9ece6a gui=bold

  sign define DiagnosticSignError linehl= numhl=DiagnosticLineNrError
  sign define DiagnosticSignWarn linehl= numhl=DiagnosticLineNrWarn
  sign define DiagnosticSignInfo linehl= numhl=DiagnosticLineNrInfo
  sign define DiagnosticSignHint linehl= numhl=DiagnosticLineNrHint
  ]]

  lsp_highlight_document(client)
  local bufopts = { noremap=true, silent=true, buffer=bufnr, }
  vim.keymap.set('n', '<leader><leader>K', vim.lsp.buf.hover, bufopts)
  vim.keymap.set('n', '<leader><leader>D', vim.diagnostic.open_float, bufopts)
  vim.keymap.set('n', '<leader><leader>dn', vim.diagnostic.goto_next, bufopts)
  vim.keymap.set('n', '<leader><leader>dp', vim.diagnostic.goto_prev, bufopts)
  vim.keymap.set('n', '<leader><leader>gd', vim.lsp.buf.definition, bufopts)
  vim.keymap.set('n', '<leader><leader>gD', vim.lsp.buf.declaration, bufopts)
  vim.keymap.set('n', '<leader><leader>rn', vim.lsp.buf.rename, bufopts)
end

local lspconfig = require('lspconfig')
local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true
for _, server in pairs({'pyright', 'lua_ls', 'bashls', 'html', 'cssls', 'tsserver', 'emmet_ls', 'eslint'}) do
  lspconfig[server].setup {
    on_attach = on_attach,
    handlers = handlers,
    capabilities = capabilities
  }
end

lspconfig.lua_ls.setup({
  on_attach = on_attach,
  handlers = handlers,
  capabilities = capabilities,
  settings = {
    Lua = {
      diagnostics = {
        globals = {'vim'},
      },
    },
  },
})
