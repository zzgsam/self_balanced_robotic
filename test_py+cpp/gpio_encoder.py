from ctypes import *
import RPi.GPIO as GPIO 
from time import sleep
#GPIO.cleanup()
#load the shared object file
class return_value_struc(Structure):
	_fields_=[
	('duration',c_int),
	('value_inter',c_int),
	]

gpio_test = CDLL('./gpio_test.so')
gpio_test.pyReturnStructure.restype=POINTER(return_value_struc)

#set encoder
#GPIO.setup(16,GPIO.IN) #Phase A IO16
#GPIO.setup(18,GPIO.IN) #Phase B IO18

#set motoer
#GPIO.setup(36,GPIO.OUT) #PWM IO36
#GPIO.setup(38,GPIO.OUT) #AIN1 IO38
#GPIO.setup(40,GPIO.OUT) #AIN2 IO40

#GPIO.output(38,0)
#GPIO.output(40,1)


#Initialization
a=gpio_test.ini()

gpio_test.pySet_PinMode(16,0)#Phase A IO16 IN
gpio_test.pySet_PinMode(18,0)#Phase B IO18 IN
gpio_test.pySet_PinMode(38,1)#AIN1 IO38 OUT
gpio_test.pySet_PinMode(40,1)#AIN2 IO40 OUT

gpio_test.pyDigitalWrite(38,0)
gpio_test.pyDigitalWrite(40,1)


#gpio_test.pySet_PinMode(5,0)
#gpio_test.pySet_PinMode(7,1)
#gpio_test.pySet_PinMode(3,4)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT) #PWM IO36
p=GPIO.PWM(36,80)
p.start(100)

#gpio_test.pySoftPwmCreate(3,100,100)
#gpio_test.pySoftPwmWrite(3,50)
gpio_test.pySetInterrupt(16,2) #Phase A IO16 GPIO.Rising

#temppp=return_value_struc()

last_temp=0
num=0
while True:
#	gpio_test.pyDigitalWrite(7,0)
#	print(gpio_test.pyReadDuration())
	period_test=gpio_test.pyReadPeriod()
	sleep(1)
	print(period_test)
	#temppp=gpio_test.pyReturnStructure()
	#print(temppp.contents.duration)
	#print(temppp.contents.duration)
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
