import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  
  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN)    # set GPIO25 as input (button)  
  
def my_callback(channel):  
    if GPIO.input(4):     # if port 25 == 1  
        print ("Rising edge detected on 25")  
    else:                  # if port 25 != 1  
        print ("Falling edge detected on 25")  
  
# when a changing edge is detected on port 25, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(4, GPIO.BOTH, callback=my_callback)  


#while True:
#	my_callback
	
	
try:  

    sleep(30)         # wait 30 seconds  
    print ("Time's up. Finished!")  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()   

