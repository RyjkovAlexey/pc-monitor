import logging
from typing import List

from loader import PluginLoader, PluginError


class Application:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.plugins: List[PluginLoader] = []
        for loader in PluginLoader.enumerate():
            try:
                plugin = PluginLoader(self.log, loader)
            except PluginError:
                self.log.error('Не удалось загрузить "%s"', loader, exc_info=True)
            else:
                self.plugins.append(plugin)

        for loader in self.plugins:
            result = loader.plugin.collect_information()
            for key in result.keys():
                print(f'{key.feature_name}\t{key.description}\t{result[key]}')


if __name__ == '__main__':
    app = Application()
