local function map(mode, combo, mapping, opts)
  local options = {noremap = true}
  if opts then
    options = vim.tbl_extend('force', options, opts)
  end
  vim.api.nvim_set_keymap(mode, combo, mapping, options)
end

map('n', '<S-J>', ':bp<CR>', { silent = true })
map('n', '<S-K>', ':bn<CR>', { silent = true })
map('n', '<C-Q>', ':bd<CR>', { silent = true })
map('n', '<esc>', ':noh<return><esc>', { silent = true, noremap = true })
map('i', '<C-J>', 'pumvisible() ? "<C-n>" : "<Tab>"', { expr = true, noremap = true })
map('i', '<C-K>', 'pumvisible() ? "<C-p>" : "<S-Tab>"', { expr = true, noremap = true })

map('v', '<leader>p', '"_dP')
map('n', '<leader>y', '"+y')
map('v', '<leader>y', '"+y')
map('n', '<leader>Y', 'gg"+yG')
map('n', '<leader>d', '"_d')
map('v', '<leader>d', '"_d')

-- Telescope Keybindings
map('n', '<leader>ff', '<cmd>Telescope find_files<cr>', { noremap = true })
map('n', '<leader>fg', '<cmd>Telescope live_grep<cr>', { noremap = true })
map('n', '<leader>fb', '<cmd>Telescope buffers<cr>', { noremap = true })
map('n', '<leader>fh', '<cmd>Telescope help_tags<cr>', { noremap = true })

-- Dap Keybindings
map('n', '<F5>', ':lua require"dap".continue()<CR>', { noremap = true })
map('n', '<F10>', ':lua require"dap".step_over()<CR>', { noremap = true })
map('n', '<F11>', ':lua require"dap".step_into()<CR>', { noremap = true })
map('n', '<F12>', ':lua require"dap".step_out()<CR>', { noremap = true })
map('n', '<leader>b', ':lua require"dap".toggle_breakpoint()<CR>', { noremap = true })
map('n', '<leader>dr', ':lua require"dap".repl.open()<CR>', { noremap = true })
map('n', '<leader>dl', ':lua require"dap".run_last()<CR>', { noremap = true })
