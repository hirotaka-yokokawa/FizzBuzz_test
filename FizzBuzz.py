import unittest


def Fizz_Buzz(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 5 == 0:
        return "Buzz"

    if number % 3 == 0:
        return "Fizz"

    return number

for number in range (1, 101):
    print(Fizz_Buzz(number))


