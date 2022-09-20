#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    last_digit = number % 10
    number *= -1
    last_digit *= -1
else:
    last_digit = number % 10
print("Last digit of", number, "is", end=" ")
if last_digit > 5:
    print(last_digit, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(last_digit, "and is less than 6 and not 0")
else:
    print(last_digit, "and is 0")
