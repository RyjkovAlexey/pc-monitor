import abc
from typing import Callable


class BasePlugin(abc.ABC):
    class BaseCharacteristic(abc.ABC):
        @property
        @abc.abstractmethod
        def feature_name(self) -> str:
            '''Возвращает название характеристики'''

        @property
        @abc.abstractmethod
        def description(self) -> str:
            '''Возвращает описание характеристики'''

        @property
        @abc.abstractmethod
        def checked(self) -> bool:
            '''Возвращает True если характеристика выбрана для сбора'''

        @checked.setter
        @abc.abstractmethod
        def checked(self, val: bool) -> None:
            '''Позволяет выбрать/отменить характеристику для сбора'''

        @property
        @abc.abstractmethod
        def collection(self) -> Callable[[], str]:
            '''Запускает сбор информации'''

        def run_collection(self) -> str:
            return self.collection()

    @property
    @abc.abstractmethod
    def name(self) -> str:
        '''Возвращает имя плагина'''

    @property
    @abc.abstractmethod
    def description(self) -> str:
        '''Возвращает описание плагина'''

    @property
    @abc.abstractmethod
    def is_on(self) -> bool:
        '''Возвращает состояние активности плагина'''

    @is_on.setter
    @abc.abstractmethod
    def is_on(self, val: bool):
        '''Устанавливает значение активности плагина'''

    @property
    @abc.abstractmethod
    def all_characteristic(self) -> [BaseCharacteristic]:
        '''Возвращает список характеристик'''

    @abc.abstractmethod
    def set_checked_for_characteristic(self, characteristic: BaseCharacteristic, value: bool):
        characteristic.checked = value

    @abc.abstractmethod
    def collect_information(self) -> dict[BaseCharacteristic, str]:
        '''Собирает всю информацию по отмеченным характеристикам и возвращает словарь'''
