import myGPIO as kit

kit.GPIO.setup(17, kit.GPIO.OUT)
kit.GPIO.setup(4, kit.GPIO.IN)
kit.GPIO.output(17, 1)

isEgual = False
while True:
    for i in range(255):
        kit.num2dac(i)
        if (kit.GPIO.input(4) >= 1):
            print('Digital value:', i, 'Analog value:', i/256*3.3)
            break


kit.GPIO.cleanup()