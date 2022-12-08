import abc


class CharacteristicAbc(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def is_selected(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def description(self) -> str:
        ...

    @name.setter
    @abc.abstractmethod
    def name(self, val: str) -> None:
        self.name = val

    @is_selected.setter
    @abc.abstractmethod
    def is_selected(self, val: bool) -> None:
        self.is_selected = val

    @description.setter
    @abc.abstractmethod
    def description(self, val: str) -> None:
        self.description = val
