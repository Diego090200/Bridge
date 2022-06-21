from Remote.remote import Remote
from Device.device import Device

class AdvancedRemote(Remote):
    def __init__(self, device: Device):
        super().__init__(device)
        self.device: Device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        if self.device.get_volume() == 0:
            print("No puede bajar el voluen ya que es 0")
        else:
            volumen: int = self.device.get_volume()
            volumen -= 1
            self.device.set_volume(volumen)

    def volume_up(self):
        if self.device.get_volume() == 100:
            print("No puede bajar el voluen ya que es 0")
        else:
            volumen: int = self.device.get_volume()
            volumen += 1
            self.device.set_volume(volumen)

    def channel_down(self):
        self.device.

    def chanenel_up(self):
        pass

    def mute(self):
        pass
