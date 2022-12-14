import logging
from typing import List

from arg_helper import ArgHelper
from loader import PluginLoader, PluginError
from normal_mode import NormalMode
from silence_mode_app import SilenceModeApp


class Application:
    @property
    def loaders(self) -> List[PluginLoader]:
        return self._loaders

    def __init__(self):
        arg_helper = ArgHelper()
        if arg_helper.mode == 'silence' or arg_helper.mode == 'normal':
            self._init_plugins()
            if arg_helper.mode == 'silence':
                SilenceModeApp(arg_helper.export_path, self.loaders).run()
            else:
                NormalMode(self.loaders)
        else:
            raise Exception(f'Режим: {arg_helper.mode} не поддерживается')

    def _init_plugins(self):
        self._log = logging.getLogger(self.__class__.__name__)
        self._loaders: List[PluginLoader] = []
        for loader in PluginLoader.enumerate():
            try:
                plugin = PluginLoader(self._log, loader)
            except PluginError:
                self._log.error('Не удалось загрузить "%s"',
                                loader, exc_info=True)
            else:
                self._loaders.append(plugin)


if __name__ == '__main__':
    app = Application()
