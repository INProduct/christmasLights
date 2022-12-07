from neopixel import NeoPixel
from machine import Pin


class Strip:
    """
    class Strip contains the Logic for a NeoPixel Strip
    """
    def __init__(self, pin, strip_len):
        self._pin = Pin(pin, Pin.OUTPUT)
        self._neopixel = NeoPixel(self._pin, self._length)
        self._length = strip_len

    def get_length(self):
        return self._length

    def clear(self):
        for i in range(self._length):
            self._neopixel[i] = (0, 0, 0)
        self._neopixel.write()

    def write(self, strip):
        for i, s in enumerate(strip):
            self._neopixel[i] = s
        self._neopixel.write()



