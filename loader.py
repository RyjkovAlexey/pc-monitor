import typing as t
import importlib
import logging
import pathlib
import sys
import tkinter as tk

from base_plugin import BasePlugin


class PluginError(Exception):
    """Исключение для сигнализации об ошибках плагинов."""
    pass


class PluginLoader:
    PLUGIN_DIR = 'plugins'

    @classmethod
    def enumerate(cls):
        plugin_path = pathlib.Path(sys.argv[0]).parent.resolve() / cls.PLUGIN_DIR
        return [path.stem for path in plugin_path.glob('*.py') if not path.name.startswith('_')]

    def __init__(self, log: logging.Logger, plugin: str):
        self._controls: t.List[tk.Widget] = []
        self._log = log
        self.plugin_name: str = plugin
        self.plugin: t.Optional[BasePlugin] = None
        try:
            module = importlib.import_module(f'{self.PLUGIN_DIR}.{plugin}')
            self.plugin: BasePlugin = module.Plugin()

        except Exception as err:
            raise PluginError(f"Ошибка при инициализации плагина {plugin}") from err

    def log(self, text: str, level=None):
        if level is None:
            level = logging.INFO
        self._log.log(level, '[%s] %s', self.plugin_name, text)
