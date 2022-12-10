import argparse


class ArgHelper:
    @property
    def mode(self) -> str:
        return self._arg.mode

    @property
    def export_path(self) -> str:
        return self._arg.export_path

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='Утилита сбора информации о системе',
            description='Утилита позволяет собирать разную информацию о системе при помощи плагинов которые вы можете реализовать самостоятельно',
        )
        ArgHelper._init_arguments_key(parser)
        self._arg = parser.parse_args()

    @staticmethod
    def _init_arguments_key(parser: argparse.ArgumentParser):
        parser.add_argument('-m', '--mode', default='normal',
                            help='Выбор режима работы утилиты, возможно два значения [-mode silence] и [-mode normal], по умолчанию установлен normal')
        parser.add_argument('-exp_path', '--export_path', default='./reports',
                            help='Укажите путь к дирректории, в которую необходимо выгрузить отчет')
