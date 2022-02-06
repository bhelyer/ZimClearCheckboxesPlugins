from zim.plugins import PluginClass
from zim.actions import action
from zim.formats import UNCHECKED_BOX

from zim.gui.pageview import PageViewExtension

class ClearCheckboxesPlugin(PluginClass):
    plugin_info = {
        'name': _('Clear Checkboxes'),
        'description': _('Clear checkboxes in a page'),
        'author': 'Bernard Helyer',
    }

class ClearCheckboxesPageViewExtension(PageViewExtension):
    @action('Clear Checkboxes', _('Clear Checkboxes'))
    def clear(self):
        buf = self.pageview.textview.get_buffer()
        for line in range(0, buf.get_line_count()):
            buf.toggle_checkbox(line, UNCHECKED_BOX)