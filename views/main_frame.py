from tkinter import *
from tkinter import ttk
from typing import List, Callable

from base_plugin import BasePlugin


class MainFrame(Frame):

    def __init__(self, plugins: List[BasePlugin], next: Callable[[], None]):
        super().__init__(width=800)

        ttk.Label(self, text='Набор плагинов', padding=10).pack()

        self.selected_plugins = {}
        self._next = next

        for plugin in plugins:
            self.selected_plugins[plugin] = BooleanVar()
            self.selected_plugins[plugin].set(plugin.is_on)

            plugin_frame = Frame(self, pady=5, padx=5)
            plugin_frame.pack(anchor='center')
            Label(plugin_frame, text=plugin.name, justify='center').grid(column=0, row=0)
            Label(plugin_frame, text=plugin.description, justify='center').grid(column=1, row=0)
            Checkbutton(plugin_frame, variable=self.selected_plugins[plugin]).grid(column=2, row=0)

        Button(self, text='Перейти к выбору характеристик', command=self._on_submit).pack()

    def _on_submit(self):
        for plugin in self.selected_plugins.keys():
            plugin.is_on = self.selected_plugins[plugin].get()

        self._next()
