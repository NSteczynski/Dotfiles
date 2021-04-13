call plug#begin('~/.config/nvim/plugged')

Plug 'sainnhe/gruvbox-material'
Plug 'sheerun/vim-polyglot'
Plug 'nvim-treesitter/nvim-treesitter', { 'do': ':TSUpdate' }
Plug 'vim-airline/vim-airline'
Plug 'tpope/vim-fugitive'
Plug 'b3nj5m1n/kommentary'
Plug 'neovim/nvim-lspconfig'
Plug 'nvim-lua/completion-nvim'
Plug 'lervag/vimtex'
Plug 'norcalli/nvim-colorizer.lua'
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

call plug#end()

syntax on

set hidden
set nobackup
set nowritebackup
set termguicolors
set noswapfile
set expandtab
set smarttab
set smartindent
set cursorline
set noerrorbells
set confirm
set nowrap
set nu
set autoindent
set smartcase
set undofile
set incsearch
set relativenumber
set cmdheight=2
set tabstop=2
set softtabstop=0
set shiftwidth=2
set updatetime=50
set scrolloff=15
set sidescrolloff=30
set t_Co=256
set colorcolumn=80
set shortmess+=c
set signcolumn=yes
set background=dark
set clipboard+=unnamedplus

let mapleader = ' '
let g:gruvbox_material_background = 'hard'

colorscheme gruvbox-material

nmap <silent><S-J> :bp<CR>
nmap <silent><S-K> :bn<CR>
nmap <silent><C-Q> :bd<CR>
nnoremap <silent> <esc> :noh<return><esc>
inoremap <expr> <C-J> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <C-K> pumvisible() ? "\<C-p>" : "\<S-Tab>"

vnoremap <leader>p "_dP
nnoremap <leader>y "+y
vnoremap <leader>y "+y
nnoremap <leader>Y gg"+yG
nnoremap <leader>d "_d
vnoremap <leader>d "_d

autocmd FileType python set shiftwidth=2 tabstop=2 expandtab
