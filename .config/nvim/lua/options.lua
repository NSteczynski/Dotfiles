vim.cmd('syntax enable')

vim.opt.hidden = true
vim.opt.backup = false
vim.opt.writebackup = false
vim.opt.termguicolors = true
vim.opt.swapfile = false
vim.opt.expandtab = true
vim.opt.smarttab = true
vim.opt.smartindent = true
vim.opt.cursorline = true
vim.opt.errorbells = false
vim.opt.confirm = true
vim.opt.wrap = false
vim.opt.nu = true
vim.opt.autoindent = true
vim.opt.smartcase = true
vim.opt.undofile = true
vim.opt.incsearch = true
vim.opt.relativenumber = true
vim.opt.cmdheight = 2
vim.opt.tabstop = 2
vim.opt.softtabstop = 0
vim.opt.shiftwidth = 2
vim.opt.updatetime = 50
vim.opt.scrolloff = 15
vim.opt.sidescrolloff = 30
vim.opt.colorcolumn = '80'
vim.opt.shortmess = vim.opt.shortmess + 'c'
vim.opt.background = 'dark'
vim.opt.clipboard = vim.opt.clipboard + 'unnamedplus'

vim.g.gruvbox_material_background = 'hard'
vim.cmd('colorscheme gruvbox-material')
