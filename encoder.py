import wiringpi as w_timer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

pulse_a=0
t1=0
t2=0
def encoder_detect(channel):
	global pulse_a,t1,t2
	pulse_a += 1
	if pulse_a==1:
		t1=w_timer.micros()
		t1=w_timer.micros()
		t2=0
#	if pulse_a==210+1:
	if pulse_a==330+1:
		t1_temp=t2=w_timer.micros()
		print(((t2-t1)/1000))
		pulse_a=1
		t1=t1_temp
#	print(pulse_a)
#set encoder
GPIO.setup(16,GPIO.IN) #Phase A IO16
GPIO.setup(18,GPIO.IN) #Phase B IO18

#set motoer
GPIO.setup(36,GPIO.OUT) #PWM IO36
GPIO.setup(38,GPIO.OUT) #AIN1 IO38
GPIO.setup(40,GPIO.OUT) #AIN2 IO40


GPIO.output(38,0)
GPIO.output(40,1)
p=GPIO.PWM(36,50)
p.start(50)
GPIO.add_event_detect(16,GPIO.RISING,callback=encoder_detect)
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
