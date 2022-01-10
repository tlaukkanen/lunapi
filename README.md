# LunaPi - RPi Powered Rover Bot

Here we have snippets of code related to Raspberry Pi powered rover bot.

Requirements:
 - Raspberry Pi, with
   - python3, python3-pip, python-smbus
   - adafruit-circuitpython-servokit, adafruit-circuitpython-motorkit
 - WaveShare Motor Driver Hat
 - Adafruit 16 Channel Servo Driver Hat
 - Raspberry Camera v1.3
 - LED Matrix 16x8

# Installing dependencies

```
sudo pip3 install adafruit-circuitpython-ssd1306 \
  adafruit-circuitpython-servokit \
  adafruit-circuitpython-motorkit \
  pillow \
  Bluetin_Echo \
  luma.led_matrix \
  python3-picamera

sudo apt-get install python3-pil libopenjp2-7
```


# Usage

sudo python3 tracktor.py

