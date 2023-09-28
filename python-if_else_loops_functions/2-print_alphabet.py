#!/usr/bin/python3
for ascii_letters in range(97, 123):
    if ascii_letters == 101 or ascii_letters == 113:
        continue
    print("{:c}".format(ascii_letters), end="")
