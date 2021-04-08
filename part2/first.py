import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(pins, GPIO.OUT)

def num2dac(decNumber):
    stroke = "{0:b}".format(decNumber)
    stroke = stroke.zfill(8)
    result = list(stroke)
    for i in range(8):
        GPIO.output(pins[i], ord(result[i]) - 48)

while 1:
    print('Please insert a number')
    number = int(input())
    num2dac(number)