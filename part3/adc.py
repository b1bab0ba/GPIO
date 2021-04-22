import myGPIO as kit

kit.GPIO.setup(17, kit.GPIO.OUT)
kit.GPIO.setup(4, kit.GPIO.IN)
kit.GPIO.output(17, 1)

isEgual = False
while True:
    i = 0
    kit.num2dac(0)

    while kit.GPIO.input(4) == kit.GPIO.HIGH:
        i += 1
        kit.num2dac(i)
        kit.time.sleep(0.001)

    print('Digital value:', i, 'Analog value:', i/256*3.3)
        


kit.GPIO.cleanup()