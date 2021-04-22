import myGPIO as kit

kit.GPIO.setup(17, kit.GPIO.OUT)
kit.GPIO.output(17, 1)

print('Please enter a number')
number = int(input())
print(number, '=', number/256*3.3, 'V')
kit.num2dac(number) 
while number > 0:
    print('Please enter a number')
    number = int(input())
    print(number, '=', number/256*3.3, 'V')
    kit.num2dac(number)

kit.GPIO.cleanup()