#!/usr/bin/python3
for character in range(97, 123):
    if (chr(character) not in ['q', 'e']):
        print("{:c}".format(character), end='')
print()
