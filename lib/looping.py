#!/usr/bin/env python3

def happy_new_year():
    countdown = 10

    while countdown > 0:
        print(countdown)
        countdown -= 1

    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    squared_numbers = [num ** 2 for num in int_list]
    return squared_numbers


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()

