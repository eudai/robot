import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(18, 50)
p1 = GPIO.PWM(12, 50)
#dr = input ("What direction?:")
#tm = input ("How long?:")


def forward():
	p.start(50)
	p1.start(75)
	GPIO.output(15, 1)
	GPIO.output(16, 0)
	GPIO.output(23, 0)
	GPIO.output(24, 1)
	time.sleep(3)

def reverse():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 1)
    GPIO.output(23, 1)
    GPIO.output(24, 0)
    time.sleep(3)

def right_arch():
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 1)
    time.sleep(3)
    
def left_arch():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 1)
    GPIO.output(16, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    time.sleep(3)

def left_pivot():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 1)
    GPIO.output(16, 0)
    GPIO.output(23, 1)
    GPIO.output(24, 0)
    time.sleep(3)

def right_pivot():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 1)
    GPIO.output(23, 0)
    GPIO.output(24, 1)
    time.sleep(3)
    
forward()
reverse()
right_arch()
left_arch()
left_pivot()
right_pivot()
print ("Hi chris")

GPIO.cleanup()
