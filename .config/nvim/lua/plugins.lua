return require('packer').startup(function()
	use 'sainnhe/gruvbox-material'
  use 'neovim/nvim-lspconfig'
  use { 'ms-jpq/coq_nvim', branch = 'coq' }
  use 'norcalli/nvim-colorizer.lua'
  use 'b3nj5m1n/kommentary'
  use 'hoob3rt/lualine.nvim'
  use 'mfussenegger/nvim-dap'
  use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }
  use {
    'nvim-telescope/telescope.nvim',
    requires = { {'nvim-lua/plenary.nvim'} }
  }
end)
