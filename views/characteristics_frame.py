from tkinter import *
from tkinter import ttk

from tkinter import Frame
from typing import List, Callable

from base_plugin import BasePlugin


class CharacteristicsFrame(Frame):
    def __init__(self, plugins: List[BasePlugin], next: Callable[[], None]):
        super().__init__()

        ttk.Label(self, text='Выбор характеристик', padding=10).pack()

        self._characteristic_variables = {}
        self._next = next

        for plugin in plugins:
            characteristics: List[BasePlugin.BaseCharacteristic] = plugin.all_characteristic

            plugin_frame = Frame(self, pady=5, padx=5)
            plugin_frame.pack(anchor='center')

            for characteristic in characteristics:
                characteristic_frame = Frame(plugin_frame, padx=5, pady=5)
                characteristic_frame.pack(anchor='center')
                self._characteristic_variables[characteristic] = BooleanVar()
                self._characteristic_variables[characteristic].set(characteristic.checked)

                Label(characteristic_frame, text=characteristic.feature_name).grid(column=0, row=0)
                Label(characteristic_frame, text=characteristic.description).grid(column=1, row=0)
                Checkbutton(characteristic_frame,
                            onvalue=True,
                            offvalue=False,
                            variable=self._characteristic_variables[characteristic],
                            ).grid(column=2, row=0)

        ttk.Button(self, text='Сформировать отчет', command=self._on_submit).pack()

    def _on_submit(self):
        for characteristic in self._characteristic_variables.keys():
            characteristic.checked = self._characteristic_variables[characteristic].get()

        self._next()
