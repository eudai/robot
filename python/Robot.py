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

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(14, GPIO.IN)    # set GPIO25 as input (button)  


def forward():
	p.start(50)
	p1.start(75)
	GPIO.output(15, 1)
	GPIO.output(16, 0)
	GPIO.output(23, 0)
	GPIO.output(24, 1)

def reverse():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 1)
    GPIO.output(23, 1)
    GPIO.output(24, 0)

def right_arch():
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 1)
    
def left_arch():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 1)
    GPIO.output(16, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 0)

def left_pivot():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 1)
    GPIO.output(16, 0)
    GPIO.output(23, 1)
    GPIO.output(24, 0)

def right_pivot():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 1)
    GPIO.output(23, 0)
    GPIO.output(24, 1)

def stop_moving():
    p1.start(75)
    p.start(50)
    GPIO.output(15, 0)
    GPIO.output(16, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 0)

    
def test_sequence():
    seq = [forward,reverse,left_arch,right_arch,left_pivot,right_pivot]
    for i in seq:
        seq[i]()
        time.sleep(3)
    stop_moving()
    print ("test complete.")

def edge_detected(channel):  
    print(channel)
    if GPIO.input(14):     # if port 4 == 1  
        print ("Rising edge detected on 14")
        stop_moving()
        right_pivot()
    else:                  # if port 25 != 1  
        print ("Falling edge detected on 14")
        start_moving()

  
# when a changing edge is detected on port 4, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(14, GPIO.BOTH, callback=edge_detected)  

time.sleep(30)

GPIO.cleanup()
print('goodbye.')
