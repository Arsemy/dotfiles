vim.cmd [[packadd packer.nvim]]

return require('packer').startup({function(use)
  use 'wbthomason/packer.nvim'

  -- Fuzzy finder with previewer.
  use {
    'nvim-telescope/telescope.nvim', branch = '0.1.x',
    requires = { 'nvim-lua/plenary.nvim' }
  }

  -- Undo tree (Telescope extension).
  use 'debugloop/telescope-undo.nvim'

  -- Colorscheme.
  use 'folke/tokyonight.nvim'

  -- Highlighting and code interpretation.
  use {
    'nvim-treesitter/nvim-treesitter',
    run = ':TSUpdate'
  }

  -- Fast jump on working files.
  use 'ThePrimeagen/harpoon'

  -- Explorer tree.
  use {
    'nvim-neo-tree/neo-tree.nvim',
    branch = 'v2.x',
    requires = {
      'nvim-lua/plenary.nvim',
      'nvim-tree/nvim-web-devicons',
      'MunifTanjim/nui.nvim',
    }
  }

  -- Status line.
  use {
    'nvim-lualine/lualine.nvim',
    requires = { 'kyazdani42/nvim-web-devicons', opt = true }
  }

  -- Shortcuts for comment.
  use 'numToStr/Comment.nvim'

  -- Indentation lines.
  use 'lukas-reineke/indent-blankline.nvim'

  -- RGB and HEX Colors with background.
  use 'NvChad/nvim-colorizer.lua'

  -- Auto close brackets, parenthesis, quotes, etc..
  use 'windwp/nvim-autopairs'

  -- Jump fast to characters.
  use 'ggandor/leap.nvim'

  -- Easy keys for surroundings
  use 'kylechui/nvim-surround'

  -- Git signs in signcolumn.
  use 'lewis6991/gitsigns.nvim'

  -- Lsp, dap, linter and formatter package manager
  use 'williamboman/mason.nvim'

  -- Lsp.
  use 'neovim/nvim-lspconfig'

  -- Auto completion.
  use {
    'hrsh7th/nvim-cmp',
    requires = {
      use 'onsails/lspkind.nvim',
    }
  }
  use 'L3MON4D3/LuaSnip'
  use 'hrsh7th/cmp-nvim-lsp'
  use 'hrsh7th/cmp-buffer'
  use 'hrsh7th/cmp-path'
  use 'hrsh7th/cmp-cmdline'

  -- Debugger.
  use 'mfussenegger/nvim-dap'
  use 'rcarriga/nvim-dap-ui'

  -- Tmux window moves integration
  use 'numToStr/Navigator.nvim'
end,

config = {
  display = {
    open_fn = function()
      return require('packer.util').float({ border = 'single', })
    end,
  },
  compile_on_sync = false,
}})
