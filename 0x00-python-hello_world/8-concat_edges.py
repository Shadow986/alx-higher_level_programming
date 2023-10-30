#!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

# Print "object-oriented programming with Python" followed by a new line
print(str.split(",")[2].split()[4][:-1])
