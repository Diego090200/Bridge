from Device.device import Device


class Remote:
    def __init__(self, device: Device):
        self.device: Device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
            print('Ha apagado el dispositivo')
        else:
            self.device.enable()
            print('Ha encendido el dispositivo')

    def volume_down(self) -> None:
        if self.device.is_enabled():
            if self.device.get_volume() == 0:
                print("No puede bajar el volumen porque ya es 0")
            else:
                volumen: int = self.device.get_volume()
                volumen -= 1
                self.device.set_volume(volumen)
                print(f'Volumen: {volumen + 1} -> {volumen}\nVolumen actualmente: {volumen}')
        else:
            print('Debe encender el dispositivo para interactuar con este')

    def volume_up(self) -> None:
        if self.device.is_enabled():
            if self.device.get_volume() == 100:
                print("No puede subir el volumen porque ya es 100")
            else:
                volumen: int = self.device.get_volume()
                volumen += 1
                self.device.set_volume(volumen)
                print(f'Volumen: {volumen - 1} -> {volumen}\nVolumen actualmente: {volumen}')
        else:
            print('Debe encender el dispositivo para interactuar con este')

    def channel_down(self) -> None:
        if self.device.is_enabled():
            self.device.canal_actual()
            actual: int = self.device.get_channel()
            anterior: str = self.device.canal_actual()
            if actual == 0:
                actual = self.device.get_cobertura() - 1
                self.device.set_channel(actual)
            else:
                actual -= 1
                self.device.set_channel(actual)
            nuevo: str = self.device.canal_actual()
            print(f'{anterior} -> {nuevo}\nCanal actual: {nuevo}')
        else:
            print('Debe encender el dispositivo para interactuar con este')

    def channel_up(self) -> None:
        if self.device.is_enabled():
            actual: int = self.device.get_channel()
            anterior: str = self.device.canal_actual()
            if actual == self.device.get_cobertura() - 1:
                self.device.set_channel(0)
            else:
                self.device.set_channel(actual + 1)
            nuevo: str = self.device.canal_actual()
            print(f'{anterior} -> {nuevo}\nCanal actual: {nuevo}')
        else:
            print('Debe encender el dispositivo para interactuar con este')
