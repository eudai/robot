import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) #Right motors backward
GPIO.setup(15, GPIO.OUT) #Right motors forward
GPIO.setup(23, GPIO.OUT) #Left motors backward
GPIO.setup(24, GPIO.OUT) #Left motors forward
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(2, GPIO.IN)    # set GPIO 2 as input (button)  

p = GPIO.PWM(18, 90)
p1 = GPIO.PWM(12, 90)
p.start(90)
p1.start (90)



def forward():
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	GPIO.output(23, 0)
	GPIO.output(24, 1)
	print("forward")
	
def right_pivot():
	GPIO.output(14, 1)
	GPIO.output(15, 0)
	GPIO.output(23, 0)
	GPIO.output(24, 1)
	print("right pivot")

def right_arch():
	GPIO.output(14, 0)
	GPIO.output(15, 0)
	GPIO.output(23, 0)
	GPIO.output(24, 1)
	print("right arch")
	
def left_arch():
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	GPIO.output(23, 0)
	GPIO.output(24, 0)
	print("left arch")
	
def reverse():
	GPIO.output(14, 1)
	GPIO.output(15, 0)
	GPIO.output(23, 1)
	GPIO.output(24, 0)
	print("reverse")
	
def left_pivot():
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	GPIO.output(23, 1)
	GPIO.output(24, 0)
	print("left pivot")

def stop_moving():
	GPIO.output(14, 0)
	GPIO.output(15, 0)
	GPIO.output(23, 0)
	GPIO.output(24, 0)
	print("Stop")
	
def test_sequence():
	seq = {'forward':forward,'reverse':reverse,'left_arch': left_arch,'right_arch':right_arch,'left_pivot': left_pivot,'right_pivot': right_pivot}
	for i in seq:
		seq[i]()
		time.sleep(3)
	stop_moving()
	print ("test complete.") 




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
        forward()
    else:                  # if port 2 != 1  
        # print ("Falling edge detected on 2")
        reverse()
        time.sleep(.3)
        right_pivot()
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
