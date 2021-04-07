import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(pins, GPIO.OUT)

stroke = '010111'
for i in range(6):
    print(stroke[i])

def decToBinList(decNumber):
    stroke = bin(decNumber)
    stroke = stroke.zfill(8)
    for i in range(8):
        GPIO.output(pins[i], stroke[i])
    time.sleep(10)

print('Please insert a number')
number = int(input())

decToBinList(number)
            