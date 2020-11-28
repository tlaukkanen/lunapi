import time
import random
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=RESET_PIN)
#oled.rotation = 2
# Clear display.
oled.fill(0)
oled.show()

width = oled.width
height = oled.height

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("fonts/EarlyGameBoy.ttf", 16)

offset = 0
loop_count = 5

while loop_count > 0:

    #for i in range(0, oled.height // 2):
    #    offset = (offset + 1) % oled.height
    #    oled.write_cmd(adafruit_ssd1306.SET_DISP_START_LINE | offset)
    #    oled.show()
    #    time.sleep(0.001)

    x = random.randint(0, 100)
    y = random.randint(0, 36)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #oled.fill(0)

    draw.ellipse((x,y,x+28,y+28), outline=0, fill=255)
    draw.ellipse((x+4,y+4,x+14,y+14), outline=0, fill=0)
    
    # draw.text((0, 0), "Robo R01", font=font, fill=255)
    oled.image(image)
    oled.show()

    loop_count = loop_count - 1

    wait_time = random.uniform(0.5, 4)

    time.sleep(wait_time)

    if not random.randint(0,3) % 2:
      draw.rectangle((0, 0, width, height), outline=0, fill=0)
      draw.rectangle((x+9, y+4, x+11, y+16), outline=0, fill=256)
      oled.image(image)
      oled.show()
      time.sleep(0.1)

time.sleep(5)

#echo.stop()
oled.poweroff()
