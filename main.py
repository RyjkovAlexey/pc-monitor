import logging
from typing import List

from arg_helper import ArgHelper
from loader import PluginLoader, PluginError
from silence_mode_app import SilenceModeApp


class Application:
    @property
    def plugins(self) -> list[PluginLoader]:
        return self._plugins

    def __init__(self):
        arg_helper = ArgHelper()
        if arg_helper.mode == 'silence' or arg_helper.mode == 'normal':
            self._init_plugins()
            if arg_helper.mode == 'silence':
                SilenceModeApp(arg_helper.export_path, self.plugins).run()
            else:
                ...
        else:
            raise Exception(f'Режим: {arg_helper.mode} не поддерживается')

    def _init_plugins(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._plugins: List[PluginLoader] = []
        for loader in PluginLoader.enumerate():
            try:
                plugin = PluginLoader(self._log, loader)
            except PluginError:
                self._log.error('Не удалось загрузить "%s"', loader, exc_info=True)
            else:
                self._plugins.append(plugin)


if __name__ == '__main__':
    app = Application()
