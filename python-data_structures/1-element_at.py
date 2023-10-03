#!/usr/bin/python3
def element_at(my_list, idx)
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]


def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print()
            return i
