#!/usr/bin/python3
for ascii_value in range(97, 123):
    if ascii_value == 101 or ascii_value == 113:
        continue
     print("{:chr}".format(ascii_value), end="")
