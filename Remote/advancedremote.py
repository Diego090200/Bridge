from Remote.remote import Remote
from Device.device import Device


class AdvancedRemote(Remote):
    def __init__(self, device: Device):
        super().__init__(device)
        self.device: Device = device

    def mute(self) -> None:
        if self.device.is_enabled():
            self.device.set_volume(0)
            print(f'El volumen es: {self.device.get_volume()}')
        else:
            print('Debe encender el dispositivo para interactuar con este')
