#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 4
GPIO.setup(led, GPIO.OUT)


def dot ():
	GPIO.output(led, 1)
	time.sleep(.1)
	GPIO.output(led, 0)
	time.sleep(.1)
	

def dash ():
    GPIO.output(led, 1)
    time.sleep(.5)
    GPIO.output(led, 0)
    time.sleep(.1)
    

def a():
	dot()
	dash()
	print('a')

def b():
	dash()
	dot()
	dot()
	dot()
	print('b')

def c():
	dash()
	dot()
	dash()
	dot()
	print('c')

def d():
	dash()
	dot()
	dot()
	print('d')

def e():
	dot()
	print('e')

def f():
	dot()
	dot()
	dash()
	dot()
	print('f')

def g():
	dash()
	dash()
	dot()
	print('g')

def h():
    dot()
    dot()
    dot()
    dot()
    print('h')

def i():
	dot()
	dot()
	print('i')

def j():
	dot()
	dash()
	dash()
	dash()
	print('j')
	
def k():
	dash()
	dot()
	dash()
	print('k')

def l():
	dot()
	dash()
	dot()
	dot()
	print('l')
	
def m():
	dash()
	dash()
	print('m')
	
def n():
	dash()
	dot()
	print('n')
	
def o():
	dash()
	dash()
	dash()
	print('o')
	
def p():
	dot()
	dash()
	dash()
	dot()
	print('p')
	
def q():
	dash()
	dash()
	dot()
	dash()
	print('q')
	
def r():
	dot()
	dash()
	dot()
	print('r')
	
def s():
	dot()
	dot()
	dot()
	print('s')
	
def t():
	dash()
	print('t')
	
def u():
	dot()
	dot()
	dash()
	print('u')
	
def v():
	dot()
	dot()
	dot()
	dash()
	print('v')
	
def w():
	dot()
	dash()
	dash()
	print('w')
	
def x():
	dash()
	dot()
	dot()
	dash()
	print('x')
	
def y():
	dash()
	dot()
	dash()
	dash()
	print('y')
	
def z():
	dash()
	dash()
	dot()
	dot()
	print('z')

def space():
	time.sleep(1)
	
function_dict = {' ':space, 'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g, 'h':h, 'i':i, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n, 'o':o, 'p':p, 'q':q, 'r':r, 's':s, 't':t, 'u':u, 'v':v, 'w':w, 'x':x, 'y':y, 'z':z}
message = input('Say:')
LowerCase = message.lower()
LLSplit = list(LowerCase)
for i in LLSplit:
	function_dict[i]()
	




GPIO.cleanup()
