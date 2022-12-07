from machine import Pin
from strip import Strip
import json

config_path = "config/config.json"

pin_neopixel = None
max_pixel = None

pin_brightness_up = None
pin_brightness_down = None

pin_change_mode = None

pin_speed_up = None
pin_speed_down = None

speed = None
min_speed = None
max_speed = None

brightness = None
max_brightness = None

brightness = None
speed = None
mode = None

led_strip = Strip(pin_neopixel, max_pixel)


def read_config():
    with open(config_path, "r") as file:
        config = json.loads(file.read())


def set_brightness(value: int):
    raise NotImplementedError()


def set_speed(value: int):
    raise NotImplementedError()


def set_next_mode():
    raise NotImplementedError()


def loop():
    raise NotImplementedError()


if __name__ == '__main__':
    loop()
