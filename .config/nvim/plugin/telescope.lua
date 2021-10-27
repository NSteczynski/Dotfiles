local actions = require('telescope.actions')

require('telescope').setup{
  defaults = {
    mappings = {
      i = {
        ["<esc>"] = actions.close,
        ["<C-j>"] = actions.move_selection_next,
        ["<C-k>"] = actions.move_selection_previous,
        ["<Tab>"] = actions.add_selection + actions.move_selection_better,
        ["<S-Tab>"] = actions.remove_selection + actions.move_selection_worse,
      },
    },
  }
}
