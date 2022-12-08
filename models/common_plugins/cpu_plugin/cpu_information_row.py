from models.base_plugin.information_row_abc import InformationRowAbc


class CpuInformationRow(InformationRowAbc):
    @property
    def characteristic_name(self) -> str:
        return self._characteristic_name

    @property
    def val(self) -> str:
        return self._val

    def __init__(self, char_name: str, val: str):
        self._characteristic_name = char_name
        self._val = val
