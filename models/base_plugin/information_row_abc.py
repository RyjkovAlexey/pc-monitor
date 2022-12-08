import abc


class InformationRowAbc(abc.ABC):

    @property
    @abc.abstractmethod
    def characteristic_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def val(self) -> str:
        ...

    @val.setter
    @abc.abstractmethod
    def val(self, val: str) -> None:
        self.val = val

    @characteristic_name.setter
    def characteristic_name(self, value):
        self.characteristic_name = value
