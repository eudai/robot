import RPi.GPIO as GPIO
import time
import random
left_name= input ('Left Player name?')
right_name = input ('Right Player name?')
names = [left_name, right_name]

                  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 4
right_button =14
left_button = 15
GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.output(led, GPIO.HIGH)
time.sleep(random.uniform(5,10))
GPIO.output(led, GPIO.LOW)
while True:
    if GPIO.input(left_button) == False:
        print (names [0] +" won")
        break
    if GPIO.input(right_button) == False:
        print (names [1] +" won")
        break
               
GPIO.cleanup()

