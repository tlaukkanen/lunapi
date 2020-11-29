import time
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
  
servo = kit.servo[0]

servo.angle = 90

for x in range(30):
  servo.angle = 90+x
  time.sleep(0.05)

for x in range(30):
  servo.angle = 120-x
  time.sleep(0.15)

kit.servo[0].angle = 90
