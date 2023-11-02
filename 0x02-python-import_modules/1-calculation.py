#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

add_result = add(a, b)
subtract_result = subtract(a, b)
multiply_result = multiply(a, b)
divide_result = divide(a, b)

print("Addition: {}".format(add_result))
print("Subtraction: {}".format(subtract_result))
print("Multiplication: {}".format(multiply_result))
print("Division: {}".format(divide_result))
