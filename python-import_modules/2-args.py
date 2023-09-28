#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("Número de argumento(s):", num_args, end="")
if num_args == 0:
    print(".", end="")
print("\n")

if num_args > 0:
    for i, arg in enumerate(args, start=1):
        print("Argumento", i, ":", arg)
