#!/usr/bin/python3
output = ""
for number in range(99):
    output += "{:02d}, ".format(number)
output += "{:02d}".format(99)
print(output)
