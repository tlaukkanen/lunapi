import time
from adafruit_servokit import ServoKit

from adafruit_motorkit import MotorKit

motors = MotorKit(0x40)

kit = ServoKit(channels=16)

#kit.servo[0].actuation_range = 200
kit.servo[0].angle = 90

time.sleep(1)

motors.motor2.throttle = -0.80
motors.motor1.throttle = 0.80

time.sleep(2)

motors.motor2.throttle = 0
motors.motor1.throttle = 0

#kit.servo[0].angle = 100
time.sleep(1)
#time.sleep(1)
motors.motor2.throttle = 0.50
motors.motor1.throttle = 0.50
#kit.servo[0].angle = 70
time.sleep(1)
#kit.servo[0].angle = 100
#time.sleep(2)
motors.motor2.throttle = 0
motors.motor1.throttle = 0

kit.servo[0].angle = 70
