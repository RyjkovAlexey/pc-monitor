import json
import pathlib
from datetime import datetime
from typing import Dict, Any

from base_plugin import BasePlugin
from loader import PluginLoader
from plugin_report import PluginReport


class SilenceModeApp:
    def __init__(self, export_path: str, _loaders: list[PluginLoader]):
        self._export_path = export_path
        self._loaders: list[PluginLoader] = _loaders

    def run(self):
        res = list(map(self._get_results, self._loaders))
        self._write_result_to_file(res)

    @staticmethod
    def _get_results(loader: PluginLoader) -> dict[str, Any]:
        collected_info = loader.plugin.collect_information()
        aggregate_results: Dict[str, str] = {}
        for key in collected_info.keys():
            aggregate_results[key.feature_name] = collected_info[key]

        return PluginReport(loader.plugin_name, aggregate_results).__dict__

    def _write_result_to_file(self, res: list[dict[str, Any]]):
        path = pathlib.Path(f'{self._export_path}/{datetime.now().microsecond}.json')
        print(path)
        with open(path, 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(res, ensure_ascii=False))
