import abc

from models.base_plugin.characteristic_abc import CharacteristicAbc
from models.base_plugin.information_row_abc import InformationRowAbc


class PluginAbc(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def is_on(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def description(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def characteristics(self) -> list[CharacteristicAbc]:
        ...

    @classmethod
    @abc.abstractmethod
    def collection_information(cls) -> list[InformationRowAbc]:
        ...

    @classmethod
    @abc.abstractmethod
    def on_select(cls, characteristic: CharacteristicAbc) -> None:
        ...

    @name.setter
    @abc.abstractmethod
    def name(self, val: str) -> None:
        self.name = val

    @description.setter
    @abc.abstractmethod
    def description(self, val: str) -> None:
        self.description = val

    @is_on.setter
    @abc.abstractmethod
    def is_on(self, val):
        self.is_on = val

    @characteristics.setter
    @abc.abstractmethod
    def characteristics(self, val: list[CharacteristicAbc]):
        self.characteristics = val
