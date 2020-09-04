import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
p = GPIO.PWM(13,50)
p.start(50)
p.changeDutyCycle(80)
for i in range(0,100) :
	time.sleep(1)
	p.changeDutyCycle(i)

