import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

t1 = GPIO.PWM(7, 50)

t1.start(0)

t1.ChangeDutyCycle(7.5)
time.sleep(3)
pos=[5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5]
try:
	while True:
		print("9.5")
		t1.ChangeDutyCycle(9.5)
		time.sleep(3)
		print("5.5")
		t1.ChangeDutyCycle(5.5)
		time.sleep(3)
		for i in pos:
			print i
			t1.ChangeDutyCycle(i)
			time.sleep(3)

except KeyboardInterrupt:
	print("User Cancelled")

finally:
	t1.stop()
	GPIO.cleanup()
	quit()
