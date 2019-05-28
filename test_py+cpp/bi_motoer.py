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

def rotation_round(period_signal_in_ns):
    period_signal_in_s=period_signal_in_ns/1000000
    period_rot=period_signal_in_s*330
    print("period=%f"%period_rot)
    if period_rot ==0:
        return 0
    else:
        rps=1/period_rot
        return rps
def change_rotational_speed(pwm_obj,rps):
    duty_cycle=43.88*rps+4.107
    pwm_obj.ChangeDutyCycle(duty_cycle)
    
    return 0
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
#motot 1
gpio_test.pySet_PinMode(16,0)#Encoder Phase A IO16 IN
gpio_test.pySet_PinMode(18,0)#Encoder Phase B IO18 IN
gpio_test.pySet_PinMode(38,1)#AIN1 IO38 OUT
gpio_test.pySet_PinMode(40,1)#AIN2 IO40 OUT

#motot 2
gpio_test.pySet_PinMode(29,0)#Encoder Phase A IO29 IN
gpio_test.pySet_PinMode(31,0)#Encoder Phase B IO31 IN
gpio_test.pySet_PinMode(35,1)#BIN1 IO35 OUT
gpio_test.pySet_PinMode(37,1)#BIN2 IO37 OUT

gpio_test.pyDigitalWrite(38,1)
gpio_test.pyDigitalWrite(40,0)

gpio_test.pyDigitalWrite(35,0)
gpio_test.pyDigitalWrite(37,1)

#gpio_test.pySet_PinMode(5,0)
#gpio_test.pySet_PinMode(7,1)
#gpio_test.pySet_PinMode(3,4)
#PWM setup
GPIO.setmode(GPIO.BOARD)
#motor 1
GPIO.setup(36,GPIO.OUT) #PWMA IO36
p1=GPIO.PWM(36,80)
p1.start(50)
#motor 2
GPIO.setup(33,GPIO.OUT) #PWMB IO33
p2=GPIO.PWM(33,80)
p2.start(50)
#gpio_test.pySoftPwmCreate(3,100,100)
#gpio_test.pySoftPwmWrite(3,50)
gpio_test.pySetInterrupt(16,2) #Phase A IO16 GPIO.Rising
gpio_test.pySetInterrupt(29,2) #Phase A IO29 GPIO.Rising

#temppp=return_value_struc()
p1.ChangeDutyCycle(50.5)
p2.ChangeDutyCycle(50.5)
last_temp=0
num=0
change_rotational_speed(p1,1)
change_rotational_speed(p2,1)
while True:
    temp_p=gpio_test.pyReadPeriod()
    print("round per second: %f "% rotation_round(temp_p))
    sleep(1)
#	gpio_test.pyDigitalWrite(7,0)
#	print(gpio_test.pyReadDuration())
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
