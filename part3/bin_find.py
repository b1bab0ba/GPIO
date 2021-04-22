import myGPIO as kit

kit.GPIO.setup(17, kit.GPIO.OUT)
kit.GPIO.setup(4, kit.GPIO.IN)
kit.GPIO.output(17, 1)

isEgual = False

while True:
    first = 0
    last = 128
    kit.num2dac(last)
    while first < last:
        #print('first: ', first)
        #print('last: ', last)
        if(kit.GPIO.input(4) == kit.GPIO.HIGH):
            last = int(last/2)
        else:
            first = last
            last = int(last*1.5)
        kit.num2dac(last)
        
    print('Digital value:', last, 'Analog value:', last/256*3.3)
        


kit.GPIO.cleanup()