# program for finding square root of a number
#using exponentiation operator
number = float(input("Enter your number for square root:"))
square_root = number ** 0.5
print("The square root of", number, "is", square_root)





#using math operaotor module
import math     #math module is built-in module in python
number = float(input("Enter your number for square root:"))
square_root = math.sqrt(number)
print("The square root of", number, "is", square_root)