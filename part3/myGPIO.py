import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [21, 20, 16, 12, 7, 8, 25, 24] # - pins from class
#pins = [6, 5, 22, 27, 17, 16, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)

def lightUp(ledNumber, period) :
    GPIO.output(pins[ledNumber], 1)
    time.sleep(period)
    GPIO.output(pins[ledNumber], 0)

def blink(ledNumber, blinkCount, blinkPeriod) :
    for i in range(blinkCount) :
        GPIO.output(pins[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(pins[ledNumber], 0)
        time.sleep(blinkPeriod)

def runningLight(count, period) :
    for k in range(count) :
        for i in range(8) :
            GPIO.output(pins[i], 1)
            time.sleep(period)
            GPIO.output(pins[i], 0)

def runningDark(count, period) :
    for i in range(8) :
        GPIO.output(pins[i], 1)
        
    for k in range(count) :
        for i in range(8) :
            GPIO.output(pins[i], 0)
            time.sleep(period)
            GPIO.output(pins[i], 1)

    for i in range(8) :
        GPIO.output(pins[i], 0)

def decToBinList(decNumber):
    stroke = bin(decNumber)[2:]
    stroke = stroke.zfill(8)
    result = list(stroke)
    return result


def num2dac(decNumber):
    binList = decToBinList(decNumber)
    for i in range(8):
        GPIO.output(dac[i], ord(binList[i]) - 48)
