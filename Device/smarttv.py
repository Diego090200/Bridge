from Device.device import Device
from typing import List


class SmartTv(Device):
    def __init__(self):
        self.__percent: int = 0
        self.__lista_canales: List = ['Netflix', 'Disney Plus', 'HBO', 'Star Plus']
        self.__channel: int = 0
        self.__enable: bool = False

    def is_enabled(self) -> bool:
        return self.__enable

    def disable(self) -> None:
        self.__enable = False

    def enable(self) -> None:
        self.__enable = True

    def get_volume(self) -> int:
        return self.__percent

    def set_volume(self, percent: int) -> None:
        self.__percent = percent

    def get_channel(self) -> int:
        return self.__channel

    def set_channel(self, channel: str) -> None:
        self.__channel = channel

    def get_cobertura(self) -> int:
        return len(self.__lista_canales)

    def canal_actual(self) -> str:
        return self.__lista_canales.__getitem__(self.__channel)
