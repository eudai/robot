import RPi.GPIO as GPIO
import time
from Robot.py import forward
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(18, 50)
p1 = GPIO.PWM(12, 50)
#dr = input ("What direction?:")
#tm = input ("How long?:")

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(2, GPIO.IN)    # set GPIO25 as input (button)  

p_amt = 60      # left
p1_amt = 60     # right

forward()
