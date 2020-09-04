import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pirPin = 14

GPIO.setup(pirPin, GPIO.IN)


def mouvement_detected():
    print("Motion detected")


try:
    GPIO.add_event_detected(pirPin, GPIO.RISING, callback=mouvement_detected)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
