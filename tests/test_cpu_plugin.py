import unittest
from typing import Dict, AnyStr

from base_plugin import BasePlugin
from plugins.cpu_plugin import Plugin


class TestCpuPlugin(unittest.TestCase):
    def setUp(self) -> None:
        self.plugin = Plugin()

    def test_constructor(self):
        self.assertIsInstance(self.plugin, BasePlugin)

    def test_name(self):
        self.assertEqual(self.plugin.name, 'CPU Info')

    def test_description(self):
        self.assertEqual(self.plugin.description, 'Cpu Info')

    def test_checked_on(self):
        self.plugin.is_on = True
        self.assertEqual(self.plugin.is_on, True)
        self.plugin.is_on = False
        self.assertEqual(self.plugin.is_on, False)

    def test_checked_characteristic(self):
        for characteristic in self.plugin.all_characteristic:
            self.plugin.set_checked_for_characteristic(characteristic, True)
            self.assertEqual(characteristic.checked, True)
            self.plugin.set_checked_for_characteristic(characteristic, False)
            self.assertEqual(characteristic.checked, False)

    def test_collect_information(self):
        collected_info = self.plugin.collect_information()

        for characteristic in collected_info.keys():
            self.assertIsInstance(characteristic, BasePlugin.BaseCharacteristic)


if __name__ == '__main__':
    unittest.main()
