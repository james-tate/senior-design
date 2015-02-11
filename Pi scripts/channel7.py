
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
freq = 1000 #need to test this value to see what the receiver puts out
i = 1

shutoff = 7
pulse = 15

GPIO.setup(shutoff, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pulse, GPIO.OUT)
pwm = GPIO.PWM(pulse, freq)
pwm.start(1)
try:
	
	while (i != 0):
		if (GPIO.input(shutoff) != 1):
			i = 0
except KeyboardInterrupt:
	pass
pwm.stop()
print 'finished'
GPIO.cleanup()