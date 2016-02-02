import RPi.GPIO as GPIO
import time

class Motion:
		
	def init(self): #this sets up the pins for movement
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
		
	def forward(self):
		GPIO.output(14, 0)
		GPIO.output(15, 1)
		GPIO.output(23, 0)
		GPIO.output(24, 1)
		print("moving forward")
		
	def right_pivot(self):
		GPIO.output(14, 1)
		GPIO.output(15, 0)
		GPIO.output(23, 0)
		GPIO.output(24, 1)

	def right_arch(self):
		GPIO.output(14, 0)
		GPIO.output(15, 0)
		GPIO.output(23, 0)
		GPIO.output(24, 1)
		
	def left_arch(self):
		GPIO.output(14, 0)
		GPIO.output(15, 1)
		GPIO.output(23, 0)
		GPIO.output(24, 0)

	def reverse(self):
		GPIO.output(14, 1)
		GPIO.output(15, 0)
		GPIO.output(23, 1)
		GPIO.output(24, 0)

	def left_pivot(self):
		GPIO.output(14, 0)
		GPIO.output(15, 1)
		GPIO.output(23, 1)
		GPIO.output(24, 0)

	def stop_moving(self):
		GPIO.output(14, 0)
		GPIO.output(15, 0)
		GPIO.output(23, 0)
		GPIO.output(24, 0)
		
	def test_sequence(self):
		seq = {'forward':forward,'reverse':reverse,'left_arch': left_arch,'right_arch':right_arch,'left_pivot': left_pivot,'right_pivot': right_pivot}
		for i in seq:
			seq[i]()
			time.sleep(3)
		stop_moving()
		print ("test complete.")
