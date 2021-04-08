import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def sinSignal(time, frequency):
    ndarray = []
    samplingFrequency = 1000
    step = 255 / (frequency * time)
    for i in range(frequency):
        ndarray.append(step * i)
    plt.plot(ndarray)
    plt.ylabel('signal value')
    plt.show

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show
#sinSignal(1, 1000)

    