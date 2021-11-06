import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(8,GPIO.IN)
GPIO.setup(14,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
try:
while True:
# forward object detection
if GPIO.input(13):
GPIO.output(16,1)
GPIO.output(20,1)
GPIO.output(19,1)
GPIO.output(26,1)
GPIO.output(25,0)# When Obejects detects Red Light turns On
print("Front Object detected")
sleep(1)
# Backward Object detection
elif GPIO.input(12):
GPIO.output(16,1)
GPIO.output(20,1)
GPIO.output(19,1)
GPIO.output(26,1)
GPIO.output(25,0)# When Obejects detects Red Light turns On
print("Back Object detected")
sleep(1)
elif GPIO.input(2): # To move forward
GPIO.output(16,0)
GPIO.output(20,1)
GPIO.output(19,1)
GPIO.output(26,0)
print("Forward")
elif GPIO.input(3): # To move backward
GPIO.output(16,1)
GPIO.output(20,0)
GPIO.output(19,0)
GPIO.output(26,1)
print("Backward")
elif GPIO.input(14): # To turn left
GPIO.output(16,1)
GPIO.output(20,0)
GPIO.output(19,1)
GPIO.output(26,0)
print("Left")
elif GPIO.input(27): # To turn right
GPIO.output(16,0)
GPIO.output(20,1)
GPIO.output(19,0)
GPIO.output(26,1)
print("Right")
else:
GPIO.output(16,1)
GPIO.output(20,1)
GPIO.output(19,1)
GPIO.output(26,1)
GPIO.output(25,1) # When there is no Object Red Light turns Off
print("Stop")
if GPIO.input(5): #Bottom Sprinkler moves forward
GPIO.output(17,1)
GPIO.output(15,0)
print("Sprinkler1 Forward")
elif GPIO.input(6): #Bottom Sprinkler moves backward
GPIO.output(17,0)
GPIO.output(15,1)
print("Sprinkler1 Backward")
else:
GPIO.output(17,1)
GPIO.output(15,1)
if GPIO.input(7): # Top Sprinkler turns left
GPIO.output(18,1)
GPIO.output(21,0)
print("Top Sprinkler Left")
elif GPIO.input(8): # Top Sprinkler turns right
GPIO.output(18,0)
GPIO.output(21,1)
print("Top Sprinkler Right")
else:
GPIO.output(18,1)
GPIO.output(21,1)
finally:
GPIO.cleanup()