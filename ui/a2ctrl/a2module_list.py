"""
a2ctrl.module_list
"""
import logging
from PySide import QtGui, QtCore

import a2mod
import a2ctrl
import a2ctrl.qlist
import a2core
from a2ctrl.base import Ico
from a2ctrl import a2module_list_ui

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class ModuleList(QtGui.QWidget):
    selection_changed = QtCore.Signal(list)

    def __init__(self, parent):
        super(ModuleList, self).__init__(parent)
        self.a2 = a2core.A2Obj.inst()
        self.setup_ui()
        self.selection = None
        self.ui.list_widget.itemSelectionChanged.connect(self.selection_change)

    def selection_change(self):
        if not self._draw_phase:
            modules = [item._module for item in self.ui.list_widget.selectedItems()]
            self.selection_changed.emit(modules)

    def select(self, modules=None):
        self._draw_phase = True
        a2ctrl.qlist.deselect_all(self.ui.list_widget)
        selection = []
        if modules is not None:
            for item in modules:
                if isinstance(item, a2mod.Mod):
                    selection.append(item)
                    item._item.setSelected(True)
                elif isinstance(item, str):
                    srcname, modname = item.split('|', 1)
                    mod = self.a2.module_sources.get(srcname, {}).mods.get(modname, {})
                    try:
                        mod._item.setSelected(True)
                        selection.append(mod)
                    except Exception:
                        pass

        self._draw_phase = False
        if selection != self.selection:
            self.selection = selection
            self.selection_changed.emit(self.selection)

    def draw_modules(self, select=None):
        """
        Call to refill the module list with items.
        ... to match filtering, module deletion or enabling of module sources.
        """
        self._draw_phase = True
        self.ui.list_widget.clear()
        for source in self.a2.module_sources.values():
            for mod in source.mods.values():
                item = QtGui.QListWidgetItem(mod.name)
                item.setIcon(Ico('a2', scale=0.8))
                item._module = mod
                mod._item = item
                self.ui.list_widget.addItem(item)

        self._draw_phase = False

    def setup_ui(self):
        self.ui = a2module_list_ui.Ui_ModuleList()
        self.ui.setupUi(self)

        self.setLayout(self.ui.module_list_layout)

    def scroll_to(self, value):
        # TODO: was this really necessary?
#        if isinstance(value, bool):
#            a2ctrl.qlist.deselect_all(self.ui.list_widget)
#            if value:
#                item = self.ui.list_widget.item(0)
#            else:
#                item = self.ui.list_widget.item(self.ui.list_widget.count() - 1)
#            item.setSelected(True)
#            self.ui.list_widget.setCurrentItem(item)
#            self.ui.list_widget.scrollToItem(item)
        pass
