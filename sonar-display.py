import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from Bluetin_Echo import Echo

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C, reset=RESET_PIN)

# Define GPIO pin constants.
TRIGGER_PIN = 14
ECHO_PIN = 15
# Initialise Sensor with pins, speed of sound.
speed_of_sound = 315
echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound)
# Measure Distance 5 times, return average.
samples = 5

loop_count = 10

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.load_default()


While loop_count > 0

    result = echo.read('cm', samples)
    # Print result.
    print(result, 'cm')

    text = result + " cm"
    draw.text((0, 0), text, font=font, fill=255)

    loop_count = loop_count - 1

    time.sleep(1)

time.sleep(5)

echo.stop()
oled.poweroff()