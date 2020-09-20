import time
from adafruit_servokit import ServoKit

from adafruit_motorkit import MotorKit

motors = MotorKit(0x40)

kit = ServoKit(channels=16)

kit.servo[0].actuation_range = 200
kit.servo[0].angle = 100

time.sleep(1)

motors.motor2.throttle = 1.0

kit.servo[0].angle = 130

time.sleep(1)

motors.motor2.throttle = 0
kit.servo[0].angle = 100
time.sleep(1)
kit.servo[0].angle = 70
time.sleep(1)
kit.servo[0].angle = 100
