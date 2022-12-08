from models.base_plugin.characteristic_abc import CharacteristicAbc


class CpuCharacteristic(CharacteristicAbc):

    @property
    def name(self) -> str:
        return self.name

    @property
    def is_selected(self) -> bool:
        return self.is_selected

    @property
    def description(self) -> str:
        return self.description

    def __init__(self, name: str, is_selected: bool, description: str):
        self.name = name
        self.is_selected = is_selected
        self.description = description

    @name.setter
    def name(self, value):
        self._name = value

    @is_selected.setter
    def is_selected(self, value):
        self._is_selected = value

    @description.setter
    def description(self, value):
        self._description = value
