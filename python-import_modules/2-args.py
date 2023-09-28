#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print('Usage: ./03-args.py <number>')
    sys.exit(1)

num = int(args[0])

if num < 0:

    print('Negative')
elif num == 0:
    print('Zero')
elif num > 0:
    print('Positive')
else:
    print('Error')

print('Done.')
