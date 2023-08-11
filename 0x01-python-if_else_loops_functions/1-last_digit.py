#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# using formular for calculating remainder
#https://www.designcise.com/web/tutorial/how-to-get-the-last-digit-of-an-integer
#-in-python#:~:text=The%20modulo%20operator%20in%20Python,then%20add%20the%20sign%20back.
last_digit = (number - (10 * int(number / 10)))

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0\n")
