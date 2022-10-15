def fizzBuzz():
    number = int(input('enter a number: '))
    for num in range(number):
        if( num % 3 and num % 5 == 0 ):
            print('FizzBuzz')
        elif ( num % 3 == 0 ):
            print('Fizz')
        elif (num % 5 == 0):
            print('Buzz')
        else:
            print(num)

fizzBuzz()