import time
import random
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Face:
  def __init__(self):

    # Setting some variables for our reset pin etc.
    RESET_PIN = digitalio.DigitalInOut(board.D4)

    self.i2c = board.I2C()
    self.oled = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c, addr=0x3C, reset=RESET_PIN)
    #oled.rotation = 2
    
    # Clear display
    self.oled.fill(0)
    self.oled.show()

    self.width = self.oled.width
    self.height = self.oled.height

    # Create blank image for drawing.
    self.image = Image.new("1", (self.oled.width, self.oled.height))
    self.draw = ImageDraw.Draw(self.image)

    # Load a font in 2 different sizes.
    self.font = ImageFont.truetype("fonts/EarlyGameBoy.ttf", 16)

  def drawEyes(self):
    x = random.randint(0, 100)
    y = random.randint(0, 36)

    # Draw a black filled box to clear the image.
    self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
    #oled.fill(0)

    self.draw.ellipse((x,y,x+28,y+28), outline=0, fill=255)
    self.draw.ellipse((x+4,y+4,x+14,y+14), outline=0, fill=0)
    
    # draw.text((0, 0), "Robo R01", font=font, fill=255)
    self.oled.image(image)
    self.oled.show()

  def drawBlinkEyes(self):
    if not random.randint(0,3) % 2:
      self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
      self.draw.rectangle((x+9, y+4, x+11, y+16), outline=0, fill=256)
      self.oled.image(self.image)
      self.oled.show()

  def poweroff(self):
    self.oled.poweroff()