from models.base_plugin.characteristic_abc import CharacteristicAbc
from models.base_plugin.information_row_abc import InformationRowAbc
from models.base_plugin.plugin_abc import PluginAbc
from models.common_plugins.cpu_plugin.cpu_characteristic import CpuCharacteristic
import cpuinfo

from models.common_plugins.cpu_plugin.cpu_information_row import CpuInformationRow


class CpuPlugin(PluginAbc):
    @property
    def name(self):
        return self._name

    @property
    def is_on(self) -> bool:
        return self._is_on

    @property
    def description(self) -> str:
        return self._description

    @property
    def characteristics(self) -> list[CharacteristicAbc]:
        return self.characteristics

    def __init__(self):
        self._name = 'Cpu Plugin'
        self._is_on = False
        self._description = 'Getter should return or yield something'
        self._characteristics = [
            CpuCharacteristic(name='Processor manufacturer', is_selected=True, description='Who made the processor'),
            CpuCharacteristic(name='Processor model', is_selected=True, description='Processor model'),
            CpuCharacteristic(name='Number of Cores', is_selected=True, description='Number of Cores')
        ]

    @classmethod
    def collection_information(cls) -> list[InformationRowAbc]:
        return [
            CpuInformationRow(char_name='Processor manufacturer', val=cpuinfo.get_cpu_info()['vendor_id_raw']),
            CpuInformationRow(char_name='Processor model', val=cpuinfo.get_cpu_info()['brand_raw']),
            CpuInformationRow(char_name='Number of Cores', val=cpuinfo.get_cpu_info()['count'])
        ]

    @classmethod
    def on_select(cls, characteristic: CharacteristicAbc) -> None:
        characteristic.is_selected = not characteristic.is_selected

    @name.setter
    def name(self, value):
        self._name = value

    @is_on.setter
    def is_on(self, value):
        self._is_on = value

    @description.setter
    def description(self, value):
        self._description = value

    @characteristics.setter
    def characteristics(self, value):
        self._characteristics = value
