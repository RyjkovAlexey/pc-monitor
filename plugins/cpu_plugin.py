from typing import Callable, Dict, List

from cpuinfo import cpuinfo

from base_plugin import BasePlugin


class Plugin(BasePlugin):
    class Characteristic(BasePlugin.BaseCharacteristic):

        @property
        def collection(self) -> Callable[[], str]:
            return self._collection

        @property
        def feature_name(self) -> str:
            return self._feature_name

        @property
        def description(self) -> str:
            return self._description

        @property
        def checked(self) -> bool:
            return self._checked

        def __init__(self, feature_name: str, description: str, checked: bool, collection_fn: Callable[[], str]):
            self._feature_name = feature_name
            self._description = description
            self._checked = checked
            self._collection = collection_fn

        @checked.setter
        def checked(self, value: bool):
            self._checked = value

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def is_on(self) -> bool:
        return self._is_one

    @property
    def all_characteristic(self) -> List[BasePlugin.BaseCharacteristic]:
        return self._all_characteristic

    def __init__(self):
        self._name = 'CPU Info'
        self._description = 'Cpu Info'
        self._is_one = True
        self._all_characteristic = [
            self.Characteristic(
                feature_name='Производитель',
                description='Собирает информацию о производителе процессора',
                checked=True,
                collection_fn=self._collect_info_manufacturer),
            self.Characteristic(
                feature_name='Модель процессора',
                description='Собирает информацию о модели',
                checked=True,
                collection_fn=self._collect_info_model
            ),
            self.Characteristic(
                feature_name='Количество ядер процессора',
                description='Собирает информацию о количестве ядер',
                checked=True,
                collection_fn=self._collect_info_count
            )
        ]

    def set_checked_for_characteristic(self, characteristic: BasePlugin.BaseCharacteristic, value: bool):
        characteristic.checked = value

    def collect_information(self) -> Dict[BasePlugin.BaseCharacteristic, str]:
        result_dict: dict[BasePlugin.BaseCharacteristic, str] = {}

        for characteristic in self.all_characteristic:
            if characteristic.checked:
                result_dict[characteristic] = characteristic.collection()

        return result_dict

    @staticmethod
    def _collect_info_manufacturer() -> str:
        return cpuinfo.get_cpu_info()['vendor_id_raw']

    @staticmethod
    def _collect_info_model() -> str:
        return cpuinfo.get_cpu_info()['brand_raw']

    @staticmethod
    def _collect_info_count() -> str:
        return cpuinfo.get_cpu_info()['count']
