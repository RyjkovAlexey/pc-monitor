from tkinter import *
from tkinter import ttk

from typing import List
from loader import PluginLoader


class NormalMode:

    def __init__(self, loaders: List[PluginLoader]) -> None:
        self._loaders = loaders
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self._init_window()

        self.root.mainloop()

    def _init_window(self) -> None:
        ttk.Label(self.frm, text='Набор плагинов').grid(column=0, row=0)
        ttk.Label(self.frm, text='Плагины по умолчанию').grid(column=0, row=1)

        self.plugins_view = map()

    @staticmethod
    def create_plugin(plg: PluginLoader):

