from models.common_plugins.cpu_plugin.cpu_characteristic import CpuCharacteristic
from models.common_plugins.cpu_plugin.cpu_plugin import CpuPlugin


class Application:
    def __init__(self):
        cpu_plugin = CpuPlugin()
        info = cpu_plugin.collection_information()
        for x in info:
            print(f'{x.characteristic_name}: {x.val}')
            print('*'*15)


if __name__ == '__main__':
    app = Application()
