import time
import random
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

#def rounded_rectangle(self: ImageDraw, xy, corner_radius, fill=None, outline=None):

def rounded_rectangle(self: ImageDraw, color, x, y, w, h, r):    
  '''Rounds'''    
  self.ellipse((x,y,x+r,y+r),fill=color)    
  self.ellipse((x+w-r,y,x+w,y+r),fill=color)    
  self.ellipse((x,y+h-r,x+r,y+h),fill=color)    
  self.ellipse((x+w-r,y+h-r,x+w,y+h),fill=color)
  
  '''rec.s'''    
  self.rectangle((x+r/2,y, x+w-(r/2), y+h),fill=color)    
  self.rectangle((x,y+r/2, x+w, y+h-(r/2)),fill=color)

ImageDraw.rounded_rectangle = rounded_rectangle

class Face:
  def __init__(self):

    # Setting some variables for our reset pin etc.
    RESET_PIN = digitalio.DigitalInOut(board.D4)

    self.i2c = board.I2C()
    self.oled = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c, addr=0x3C, reset=RESET_PIN)
    self.oled.rotation = 1
    #self.oled.set_contrast(64)

    # Clear display
    self.oled.fill(0)
    self.oled.show()

    self.width = 32 #self.oled.width
    self.height = 128 #self.oled.height

    # Create blank image for drawing.
    self.image = Image.new("1", (32, 128))
    self.draw = ImageDraw.Draw(self.image)
    self.draw.rounded_rectangle = rounded_rectangle
    # Load a font in 2 different sizes.
    self.font = ImageFont.truetype("../fonts/EarlyGameBoy.ttf", 16)

  def drawEyes(self):
    x = random.randint(0, 12)
    y = random.randint(20, 64)

    # Draw a black filled box to clear the image.
    self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
    #oled.fill(0)

    #self.draw.ellipse((x,y,x+28,y+28), outline=0, fill=255)
    #self.draw.ellipse((x+10,y+10,x+18,y+18), outline=0, fill=0)
    self.draw.rounded_rectangle(self.draw, 255, x, y, 20, 40, 20)
    self.draw.rectangle((x, y+30, x+10, y+40), outline=0, fill=0)
    
    # draw.text((0, 0), "Robo R01", font=font, fill=255)
    
    self.oled.image(self.image)
    self.oled.show()

  def drawBlinkEyes(self):
    if not random.randint(0,3) % 2:
      self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
      self.draw.rectangle((x+9, y+4, x+11, y+16), outline=0, fill=256)
      self.oled.image(self.image)
      self.oled.show()

  def poweroff(self):
    self.oled.poweroff()

face = Face()
face.drawEyes()
time.sleep(2)
face.drawEyes()
time.sleep(2)
face.poweroff()
