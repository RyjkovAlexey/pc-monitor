from tkinter import *
from tkinter import ttk

from typing import List, Dict

from base_plugin import BasePlugin
from loader import PluginLoader
from views.characteristics_frame import CharacteristicsFrame
from views.main_frame import MainFrame
from views.report_frame import ReportFrame


class NormalMode:

    def __init__(self, loaders: List[PluginLoader]) -> None:
        self._loaders = loaders
        self._root = Tk()
        self._root.geometry('800x600')
        self._plugins: List[BasePlugin] = list(map(lambda x: x.plugin, self._loaders))

        self._current_frame: Frame = MainFrame(
            self._plugins,
            self._show_characteristic
        )

        self._current_frame.pack()

        self._root.mainloop()

    def _show_characteristic(self):
        self._current_frame.destroy()

        self._current_frame = CharacteristicsFrame(list(filter(lambda x: x.is_on, self._plugins)), self._show_reports)
        self._current_frame.pack()

    def _show_reports(self):
        reports: Dict[BasePlugin, Dict[BasePlugin.BaseCharacteristic, str]] = {}
        for plugin in self._plugins:
            reports[plugin] = plugin.collect_information()

        self._current_frame.destroy()
        self._current_frame = ReportFrame(reports)
        self._current_frame.pack()
