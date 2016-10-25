import time
import RPi.GPIO as GPIO

class controlMotor(object):

        def __init__(self, t1):
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(7, GPIO.OUT)
                self.t1 = GPIO.PWM(7, 50)
                calibraMotor()

        def calibraMotor():
                print("Calibrando motor...")
                t1.start(0)
                t1.ChangeDutyCycle(7.5)
                time.sleep(3)
                t1.ChangeDutyCycle(9.5)
                time.sleep(3)
                t1.ChangeDutyCycle(5.5)
                time.sleep(3)
                print("Calibrado motor terminado")

        def cambiaVelocidadMotor(float velocidad):
                pass        
