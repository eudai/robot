import RPi.GPIO as GPIO
import time
import picamera
import RobotMethods
import RMove *


def record():
	camera = picamera.PiCamera()
	camera.start_recording('/home/pi/Videos/test')
	


def edge_detected(channel):
	record()
    pin_active = GPIO.input(channel)
    events.append(pin_active)
    if pin_active: # if port 2 == 1  
        # print ("Rising edge detected on 2")
        forward()
    else:                  # if port 2 != 1  
        # print ("Falling edge detected on 2")
        reverse()
        time.sleep(.4)
        right_pivot()
        time.sleep(1)
  
 #when a changing edge is detected on port 2, regardless of whatever   
 #else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(2, GPIO.BOTH, callback=edge_detected)

events = []
print('hello.')
time.sleep(30)


camera.stop_recording()
print('here is what happened:')
print(events)
print('goodbye.')
GPIO.cleanup()
