#!/usr/bin/env python
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT
from luma.led_matrix.device import max7219
import time

serial = spi(port=0, device=0, gpio=noop(), block_orientation=90)
device = max7219(serial, width=16, height=8)

with canvas(device) as draw:
   draw.rectangle((1,3,4,4), outline="white")
   draw.rectangle((9,3,12,4), outline="white")
   #text(draw, (2, 1), "Hello", fill="white", font=proportional(LCD_FONT))

time.sleep(5)
