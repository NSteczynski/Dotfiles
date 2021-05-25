# Colors
backgroundLight = "#282828"
background = "#1d2021"
foreground = "#d4be98"

red     = "#ea6962"
green   = "#a9b665"
yellow  = "#d8a657"
blue    = "#7daea3"
magenta = "#d3869b"
cyan    = "#89b482"

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Time interval (in milliseconds) between auto-saves of
# config/cookies/etc.
# Type: Int
c.auto_save.interval = 10000

# Always restore open sites when qutebrowser is reopened. Without this
# option set, `:wq` (`:quit --save`) needs to be used to save open tabs
# (and restore them), while quitting qutebrowser in any other way will
# not save/restore the session. By default, this will save to the
# session which was last loaded. This behavior can be customized via the
# `session.default_name` setting.
# Type: Bool
c.auto_save.session = True

# Backend to use to display websites. qutebrowser supports two different
# web rendering engines / backends, QtWebKit and QtWebEngine. QtWebKit
# was discontinued by the Qt project with Qt 5.6, but picked up as a
# well maintained fork: https://github.com/annulen/webkit/wiki -
# qutebrowser only supports the fork. QtWebEngine is Qt's official
# successor to QtWebKit. It's slightly more resource hungry than
# QtWebKit and has a couple of missing features in qutebrowser, but is
# generally the preferred choice.
# Type: String
# Valid values:
#   - webengine: Use QtWebEngine (based on Chromium).
#   - webkit: Use QtWebKit (based on WebKit, similar to Safari).
c.backend = 'webengine'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = background

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = background

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = background

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = foreground

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = background

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = [foreground]

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = foreground

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = background

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = background

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = background

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = red

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = blue

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = backgroundLight

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = background

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = foreground

# Background color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.bg = None

# Foreground color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.fg = None

# Background color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.bg = None

# Foreground color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.fg = None

# Background color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.bg = backgroundLight

# Foreground color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.fg = foreground

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = background

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = red

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = background

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = blue

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = background

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = red

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = background

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = background

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = foreground

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = cyan

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = background

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = foreground

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = cyan

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = red

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = red

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = background

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = blue

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = blue

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = background

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = yellow

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = yellow

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = background

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = background

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = background

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = foreground

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = backgroundLight

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = red

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = background

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = red

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = background

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = background

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = foreground

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = background

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = foreground

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = green

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = background

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = background

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = foreground

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = blue

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = background

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = background

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = foreground

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = cyan

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = red

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = foreground

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = cyan

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = foreground
c.colors.statusbar.url.success.https.fg = foreground

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = yellow

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = background

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = background

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = foreground

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = red

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = blue

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = green

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = background

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = foreground

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = background

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = foreground

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = background

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = foreground

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = backgroundLight

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = foreground

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = backgroundLight

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = foreground

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = backgroundLight

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = foreground

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = backgroundLight

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = foreground

# Force `prefers-color-scheme: color` colors for websites.
# Type: "auto", "light", "dark"
c.colors.webpage.preferred_color_scheme = "dark"

# Execute the best-matching command on a partial match.
# Type: Bool
c.completion.use_best_match = True

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# c.content.notifications = False

# Allow pdf.js to view PDF files in the browser. Note that the files can
# still be downloaded by clicking the download button in the pdf.js
# viewer.
# Type: Bool
c.content.pdfjs = True

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = ['Terminus']

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
# Type: String
c.fonts.default_size = '11pt'

# Automatically enter insert mode if an editable element is focused
# after loading the page.
# Type: Bool
c.input.insert_mode.auto_load = True

# When/how to show the scrollbar.
# Type: String
# Valid values:
#   - always: Always show the scrollbar.
#   - never: Never show the scrollbar.
#   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
#   - overlay: Show an overlay scrollbar. With Qt < 5.11 or on macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
c.scrolling.bar = 'overlay'

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = False

# Padding (in pixels) for the statusbar.
# Type: Padding
c.statusbar.padding = {'top': 2, 'bottom': 2, 'left': 2, 'right': 2}

# When to show the statusbar.
# Type: String
# Valid values:
#   - always: Always show the statusbar.
#   - never: Always hide the statusbar.
#   - in-mode: Show the statusbar when in modes other than normal mode.
c.statusbar.show = 'always'

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# Padding (in pixels) for tab indicators.
# Type: Padding
c.tabs.indicator.padding = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 0

# How to behave when the last tab is closed.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'startpage'

# Switch between tabs using the mouse wheel.
# Type: Bool
c.tabs.mousewheel_switching = False

# Position of new tabs which are not opened from another tab. See
# `tabs.new_position.stacking` for controlling stacking behavior.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.unrelated = 'next'

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 10, 'right': 10}

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'last-used'

# Duration (in milliseconds) to show the tab bar before hiding it when
# tabs.show is set to 'switching'.
# Type: Int
c.tabs.show_switching_delay = 1000

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string ` - ` if a title is
# set, empty otherwise. * `{index}`: Index of this tab. *
# `{aligned_index}`: Index of this tab padded with spaces to have the
# same   width. * `{id}`: Internal tab ID of this tab. * `{scroll_pos}`:
# Page scroll position. * `{host}`: Host of the current web page. *
# `{backend}`: Either ''webkit'' or ''webengine'' * `{private}`:
# Indicates when private mode is enabled. * `{current_url}`: URL of the
# current web page. * `{protocol}`: Protocol (http/https/...) of the
# current web page. * `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = ' {current_title}'

# Hide the window decoration.  This setting requires a restart on
# Wayland.
# Type: Bool
c.window.hide_decoration = True

# Format to use for the window title. The same placeholders like for
# `tabs.title.format` are defined.
# Type: FormatString
c.window.title_format = '{perc}{title_sep}'

c.qt.highdpi = True

c.qt.args += [
    "ignore-gpu-blocklist",
    "enable-accelerated-2d-canvas",
    "enable-gpu-memory-buffer-video-frames",
    "enable-gpu-rasterization",
    "enable-native-gpu-memory-buffers",
    "enable-oop-rasterization",
    "enable-zero-copy",
]

# Bindings for normal mode
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')

# Bindings for command mode
config.bind('<CTRL-K>', 'completion-item-focus prev', mode='command')
config.bind('<CTRL-J>', 'completion-item-focus next', mode='command')
