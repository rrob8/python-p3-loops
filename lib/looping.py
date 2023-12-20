#!/usr/bin/env python3

def happy_new_year():
    i = 0
    y = 10
    while y > i:
        print(y)
        y -= 1
    
    print('Happy New Year!')


def square_integers(int_list):
    squares = [number*number for number in int_list]
    return squares

def fizzbuzz():
    i = 1
    while i <= 100:
        if (i/3).is_integer() == True and (i/5).is_integer() == True :
            print('FizzBuzz')
            i += 1
        elif (i/3).is_integer() == True:
            print('Fizz')
            i += 1
        elif (i/5).is_integer() == True:
            print('Buzz')
            i += 1
        
        else:
            print(i)
            i += 1



