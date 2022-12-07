import time


class ContextInfo:
    """

    """
    def __init__(self):
        self._millis = 0
        self._last_time = time.ticks_ms()
        self._speed = 0
        self._brightness = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value

    @property
    def millis(self):
        return self._millis

    def loop(self):
        self._millis = time.ticks_diff(time.ticks_ms(), self._last_time)
        self._last_time = time.ticks_ms()

