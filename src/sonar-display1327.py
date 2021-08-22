import time
import board
#import displayio
import digitalio
from PIL import Image, ImageDraw, ImageFont
#import adafruit_ssd1327
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1327
from Bluetin_Echo import Echo

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

serial = i2c(port=1, address=0x3C)

#display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
#oled = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)
oled = ssd1327(serial, rotate=1)

# Define GPIO pin constants.
TRIGGER_PIN = 14
ECHO_PIN = 15
# Initialise Sensor with pins, speed of sound.
speed_of_sound = 315
echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound)
# Measure Distance 5 times, return average.
samples = 5
loop_count = 5


# Clear display.
oled.clear()
oled.show()

width = oled.width
height = oled.height

# Create blank image for drawing.
image = Image.new("L", (width, height)).convert(oled.mode)
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("../fonts/EarlyGameBoy.ttf", 16)

offset = 0

while loop_count > 0:

    result = echo.read('cm', samples)
    # Print result.
    print(f"{result:4.2f} cm")

    #for i in range(0, oled.height // 2):
    #    offset = (offset + 1) % oled.height
    #    oled.write_cmd(adafruit_ssd1306.SET_DISP_START_LINE | offset)
    #    oled.show()
    #    time.sleep(0.001)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #oled.fill(0)

    draw.text((0, 0), "Robo R01", font=font, fill=255)
    text = f"{result:3.1f} cm"
    draw.text((0, 16), text, font=font, fill=255)
    oled.display(image)
    oled.show()

    loop_count = loop_count - 1

    time.sleep(1)


time.sleep(5)

echo.stop()
oled.cleanup()
