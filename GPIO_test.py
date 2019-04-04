import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12,GPIO.OUT)	
GPIO.setup(36,GPIO.OUT) #PWM IO36
GPIO.setup(38,GPIO.OUT) #AIN1 IO38
GPIO.setup(40,GPIO.OUT) #AIN2 IO40


GPIO.output(38,0)
GPIO.output(40,1)
p=GPIO.PWM(36,50)
p.start(0)
try:
	while 1:
		p.ChangeDutyCycle(90)

except KeyboardInterrupt:
	print("Error")
	pass
p.stop()
#GPIO.output(12,0)
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
