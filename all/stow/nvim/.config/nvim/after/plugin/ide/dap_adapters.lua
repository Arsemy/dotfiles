local dap = require('dap')

dap.adapters.python = {
  type = 'executable';
  command = vim.fn.stdpath('data') .. '/mason/packages/debugpy/venv/bin/python';
  args = { '-m', 'debugpy.adapter' };
}
dap.adapters.codelldb = {
  type = 'server',
  port = "${port}",
  executable = {
    command = '/home/arsemy/.local/share/nvim/mason/packages/codelldb/extension/adapter/codelldb',
    args = {"--port", "${port}"},

    -- On windows you may have to uncomment this:
    -- detached = false,
  }
}

dap.configurations.python = {
  {
    -- The first three options are required by nvim-dap.
    type = 'python'; -- The type here established the link to the adapter definition: `dap.adapters.python`.
    request = 'launch';
    name = "Launch file";

    -- Options below are for debugpy, see https://github.com/microsoft/debugpy/wiki/Debug-configuration-settings for supported options.

    program = "${file}"; -- This configuration will launch the current file if used.
    pythonPath = function()
      -- Debugpy supports launching an application with a different interpreter then the one used to launch debugpy itself.
      -- The code below looks for a `venv` or `.venv` folder in the current directly and uses the python within.
      -- You could adapt this - to for example use the `VIRTUAL_ENV` environment variable.
      local py = vim.fn.input('Python executable: ', vim.fn.getcwd() .. '/', 'file')
      if py == vim.fn.getcwd() then
        local cwd = vim.fn.getcwd()
        if vim.fn.executable(cwd .. '/venv/bin/python') == 1 then
          return cwd .. '/venv/bin/python'
        elseif vim.fn.executable(cwd .. '/.venv/bin/python') == 1 then
          return cwd .. '/.venv/bin/python'
        else
          return '/usr/bin/python'
        end
      else
        return py
      end
    end;
  },
}

dap.configurations.cpp = {
  {
    name = "Launch file",
    type = "codelldb",
    request = "launch",
    program = function()
      return vim.fn.input('Path to executable: ', vim.fn.getcwd() .. '/', 'file')
    end,
    cwd = '${workspaceFolder}',
    stopOnEntry = false,
  },
}
dap.configurations.c = dap.configurations.cpp
dap.configurations.rust = dap.configurations.cpp
