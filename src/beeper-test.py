import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
#The output pin
GPIO_PIN = 26
GPIO.setup(GPIO_PIN, GPIO.OUT)

pwm = GPIO.PWM(GPIO_PIN, 500)
# The program will wait for the input of a new frequency.


def beep(freq, seconds):
    pwm.ChangeFrequency(freq)
    pwm.start(50)
    time.sleep(seconds)
    pwm.stop()


beep(300, 0.2)
beep(400, 0.2)
beep(300, 0.2)
beep(500, 0.1)
time.sleep(0.1)
beep(300, 0.2)

GPIO.cleanup()
