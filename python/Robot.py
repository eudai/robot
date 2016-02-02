import RPi.GPIO as GPIO
import time
import picamera
from RMove import Motion

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) #Right motors backward
GPIO.setup(15, GPIO.OUT) #Right motors forward
GPIO.setup(23, GPIO.OUT) #Left motors backward
GPIO.setup(24, GPIO.OUT) #Left motors forward
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(18, 90)
p1 = GPIO.PWM(12, 90)

GPIO.setup(2, GPIO.IN)    # set GPIO2 as input (button)

p.start(90)      # left
p1.start(90)     # right
print("Motion initiallized")




motion = Motion()

#camera = picamera.PiCamera()
def record():
	camera = picamera.PiCamera()
	camera.start_recording('/home/pi/Videos/test.h264')
	


def edge_detected(channel):
 #   record()
    pin_active = GPIO.input(channel)
    events.append(pin_active)
    if pin_active: # if port 2 == 1  
        # print ("Rising edge detected on 2")
        motion.forward()
    else:                  # if port 2 != 1  
        # print ("Falling edge detected on 2")
        motion.reverse()
        time.sleep(.3)
        motion.right_pivot()
        time.sleep(.5)
  
 #when a changing edge is detected on port 2, regardless of whatever   
 #else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(2, GPIO.BOTH, callback=edge_detected)

events = []
print('hello.')
time.sleep(30)


#camera.stop_recording()
print('here is what happened:')
print(events)
print('goodbye.')
GPIO.cleanup()
