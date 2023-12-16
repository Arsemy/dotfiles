-- Show whitespace
vim.cmd('set list lcs=trail:∎')

-- Trim whitespace
function trimWhiteSpace()
    -- Save the current window view
    local save_view = vim.fn.winsaveview()

    -- Remove trailing whitespace from all lines
    vim.cmd("keeppatterns %s/\\s\\+$//e")

    -- Restore the previous window view
    vim.fn.winrestview(save_view)
end

vim.cmd([[autocmd FileType htmldjango set filetype=html]])
