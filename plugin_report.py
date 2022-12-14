from typing import Dict


class PluginReport:
    def __init__(self, plugin_name: str, result_dic: Dict[str, str]):
        self._plugin_name = plugin_name
        self._result_dict = result_dic
