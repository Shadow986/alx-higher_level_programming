#!/usr/bin/python3

import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

print('{} argument{}{}'.format(
    num_arguments, 's' * (num_arguments != 1),
    ':' if num_arguments > 0 else '.'
))

for i, argument in enumerate(arguments, start=1):
    print('{}: {}'.format(i, argument))
