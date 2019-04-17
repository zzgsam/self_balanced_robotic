from ctypes import *
import RPi.GPIO as GPIO 
#load the shared object file
gpio_test = CDLL('./gpio_test.so')

#Find sum of integers
a=gpio_test.ini()
gpio_test.pySet_PinMode(5,0)
gpio_test.pySet_PinMode(7,1)
gpio_test.pySet_PinMode(3,4)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
p=GPIO.PWM(3,800)
p.start(50)
#gpio_test.pySoftPwmCreate(3,100,100)
#gpio_test.pySoftPwmWrite(3,50)
gpio_test.pySetInterrupt(5,2)


last_temp=0
num=0
while True:
	#gpio_test.pyDigitalWrite(7,0)
	print(gpio_test.pyReadDuration())

#	temp=gpio_test.pyReadInterruptCounter()
#	if temp==last_temp:
#		last_temp=temp
#		num+=1
#	else:
#		last_temp=temp
#		print(num)
#		num=0
#	print(gpio_test.pyDigitalRead(5))
	#gpio_test.pyDigitalWrite(7,1)
#	print(gpio_test.pyDigitalRead(5))
