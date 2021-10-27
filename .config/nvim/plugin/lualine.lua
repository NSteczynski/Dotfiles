require('lualine').setup {
  options = {
    icons_enabled = false,
    theme = 'auto',
    section_separators = '',
    component_separators = ''
  },
  sections = {
    lualine_a = { 'mode' },
    lualina_b = { 'branch' },
    lualine_c = { 'filename' },
    lualine_x = { 'encoding', 'filetype' },
    lualine_y = { 'progress' },
    lualine_z = { 'location' }
  },
  inactive_sections = {
    lualine_a = {},
    lualina_b = {},
    lualine_c = { 'filename' },
    lualine_x = {},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {
    lualine_a = { 'buffers' },
    lualine_b = { 'branch' },
    lualine_c = { 'filename' },
    lualine_x = {},
    lualine_y = {},
    lualine_z = { 'tabs' }
  },
  extensions = {}
}
