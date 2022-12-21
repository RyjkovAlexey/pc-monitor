import unittest
from typing import List

from loader import PluginLoader, PluginError


class TestLoader(unittest.TestCase):
    def test_loader(self):
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
    unittest.main()
