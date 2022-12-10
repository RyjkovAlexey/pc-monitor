import json
from datetime import datetime

from base_plugin import BasePlugin
from loader import PluginLoader
from plugin_report import PluginReport


class SilenceModeApp:
    def __init__(self, export_path: str, plugins: [PluginLoader]):
        self._export_path = export_path
        self._plugins: [PluginLoader] = plugins

    def run(self):
        results: [PluginReport] = []
        for plugin in self._plugins:
            info: dict[BasePlugin.BaseCharacteristic, str] = plugin.plugin.collect_information()
            converted = {}
            for result_row in info:
                converted[result_row.feature_name] = info[result_row]
            results.append(PluginReport(plugin.plugin.name, converted).__dict__)

        with open('sample.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(results, ensure_ascii=False))
