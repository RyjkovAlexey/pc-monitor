from tkinter import *
from tkinter import ttk
from typing import Dict

from base_plugin import BasePlugin


class ReportFrame(Frame):

    def __init__(self, reports: Dict[BasePlugin, Dict[BasePlugin.BaseCharacteristic, str]]):
        super().__init__()

        ttk.Label(self, text='Отчёт', padding=15).pack()

        for plugin in reports.keys():
            characteristics = reports[plugin]

            ttk.Label(self, text=plugin.name, padding=10)

            plugin_frame = Frame(self, pady=5, padx=5, borderwidth=2)
            Label(plugin_frame, text=f'Отчет от плагина: {plugin.name}').pack()
            plugin_frame.pack(anchor='center')

            for characteristic in characteristics:
                characteristic_frame = Frame(plugin_frame, pady=3, padx=3)
                characteristic_frame.pack()
                Label(characteristic_frame, text=characteristic.feature_name).grid(column=0, row=0)
                Label(characteristic_frame, text=characteristics[characteristic]).grid(column=1, row=0)
