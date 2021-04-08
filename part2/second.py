import RPi.GPIO as GPIO
import time
import DacModule

#GPIO.setmode(GPIO.BCM)
#dacPins = [26, 19, 13, 6, 5, 11, 9, 10]
#GPIO.setup(dacPins, GPIO.OUT)

print('Insert count of cycles')
repetitionsNumber = int(input())
for i in range(repetitionsNumber):
    for i in range(256):
        DacModule.num2dac(i)
        time.sleep(0.05)
GPIO.cleanup()