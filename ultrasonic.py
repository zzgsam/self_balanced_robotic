import wiringpi as w_timer
import RPi.GPIO as GPIO

def call_back(channel):
	print("channel %d" % channel)
	t1_callback=0
	t2_callback=0
	t1_callback=w_timer.micros()
	t1_callback=w_timer.micros()
	t2_callback=w_timer.micros()
	while GPIO.input(37) == GPIO.HIGH:
		t2_callback=w_timer.micros()
#		print("test %d" %t2_callback)
	print("In callback function t2-t1=%d us" % (t2_callback-t1_callback))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT) #Trigger Pulse Input
GPIO.setup(37,GPIO.IN) #Echo Pulse Output

GPIO.add_event_detect(37,GPIO.RISING,callback=call_back)

while True:
	t1=0
	t2=0
	GPIO.output(35,1) #Enable Trigger Pulse
	t1=w_timer.micros()
	t1=w_timer.micros()
	t2=w_timer.micros()
	while t2-t1 < 10:
#		print("t2-t1=%d"% (t2-t1))
		t2=w_timer.micros()
	GPIO.output(35,0) #Enable Trigger Pulse
	t2=w_timer.micros()
#	print(t2-t1)
