import RPi GPIO as GPIO
import time
import picamera

init(): #this sets up the pins and camera for movement and video
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(14, GPIO.	OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	p = GPIO.PWM(18, 80)
	p1 = GPIO.PWM(12, 80)
	camera = picamera.PiCamera()
	camera.start_recording('/home/pi/Videos/test')
	GPIO.setup(2, GPIO.IN)    # set GPIO25 as input (button)
	p_amt = 100      # left
	p1_amt = 100     # right
	
def forward():
	init()
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	GPIO.output(23, 0)
	GPIO.output(24, 1)
	
def right_pivot():
    init()
    GPIO.output(14, 1)
    GPIO.output(15, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 1)

def right_arch():
    init()
    GPIO.output(14, 0)
    GPIO.output(15, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 1)
    
def left_arch():
    init()
    GPIO.output(14, 0)
    GPIO.output(15, 1)
    GPIO.output(23, 0)
    GPIO.output(24, 0)

def reverse():
    p1.start(p1_amt)
    p.start(p_amt)
    GPIO.output(14, 1)
    GPIO.output(15, 0)
    GPIO.output(23, 1)
    GPIO.output(24, 0)

def left_pivot():
    p1.start(p1_amt)
    p.start(p_amt)
    GPIO.output(14, 0)
    GPIO.output(15, 1)
    GPIO.output(23, 1)
    GPIO.output(24, 0)

def stop_moving():
    p1.start(p1_amt)
    p.start(p_amt)
    GPIO.output(14, 0)
    GPIO.output(15, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
