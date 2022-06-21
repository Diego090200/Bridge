from models.device import Device
from typing import List


class Tv(Device):
    def __init__(self):
        self.__percent: int = 0

    def is_enabled(self):
        return self.__enable

    def disable(self):
        self.__enable = False

    def enable(self):
        self.__enable = True

    def get_volume(self):
        return self.__percent

    def set_volume(self, percent: int):
        self.__percent = percent

    def get_channel(self):
        return self.__channel

    def set_channel(self, channel: str):
        self.__channel = channel
