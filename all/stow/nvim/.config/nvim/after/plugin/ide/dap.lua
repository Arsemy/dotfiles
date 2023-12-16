vim.keymap.set('n', '<f1>', function() require('dapui').toggle({reset = true,}) end)
vim.keymap.set('n', '<f2>', function() require('dap').step_over() end)
vim.keymap.set('n', '<f3>', function() require('dap').step_into() end)
vim.keymap.set('n', '<f4>', function() require('dap').step_out() end)
vim.keymap.set('n', '<f5>', function() require('dap').continue() end)
vim.keymap.set('n', '<leader><leader>b', function() require('dap').toggle_breakpoint() end)
-- Conditional breakpoint.
vim.keymap.set('n', '<leader><leader>B', function() require('dap').set_breakpoint(vim.fn.input('Breakpoint condition: ')) end)
vim.keymap.set('n', '<leader><leader>lp', function() require('dap').set_breakpoint(nil, nil, vim.fn.input('Log point message: ')) end)
vim.keymap.set('n', '<leader><leader>dr', function() require('dap').repl.open() end)

require("dapui").setup({
  layouts = { {
    elements = { {
      id = "breakpoints",
      size = 0.22
    }, {
      id = "watches",
      size = 0.25
    }, {
      id = "stacks",
      size = 0.25
    }, {
      id = "scopes",
      size = 0.28
    } },
    position = "left",
    size = 40
  }, {
    elements = { {
      id = "repl",
      size = 0.5
    }, {
      id = "console",
      size = 0.5
    } },
    position = "bottom",
    size = 10
  } },
})
