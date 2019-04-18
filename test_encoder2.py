import wiringpi as w_timer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

pulse_a=0
t1=0
t2=0
counter=0
def encoder_detect(channel):
	global counter
	counter+=1
	if counter % 2 == 0: 
		GPIO.output(12,1)
		for i in range(100):
			pass
		GPIO.output(12,0)
if __name__ == '__main__':
#set encoder
	GPIO.setup(16,GPIO.IN) #Phase A IO16
	GPIO.setup(18,GPIO.IN) #Phase B IO18
	GPIO.setup(37,GPIO.IN) #PWM IO37
#set motoer
	GPIO.setup(35,GPIO.OUT) #PWM IO35
	GPIO.setup(36,GPIO.OUT) #PWM IO36
	GPIO.setup(38,GPIO.OUT) #AIN1 IO38
	GPIO.setup(40,GPIO.OUT) #AIN2 IO40
	GPIO.setup(12,GPIO.OUT) #TEST IO12
	GPIO.output(38,0)
	GPIO.output(40,1)
	#p=GPIO.PWM(36,100)
	p=GPIO.PWM(35,300)
	p.start(90)
	GPIO.add_event_detect(37,GPIO.RISING,callback=encoder_detect)
	
	try:
		while 1:
	#		p.ChangeDutyCycle(90)
			pass
	except KeyboardInterrupt:
		print("Error")
		pass
	p.stop()
	GPIO.cleanup()
'''
	while 1:
		for dc in range(0,101,5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)	
		for dc in range(100,-1,-5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)	
'''
