#!/usr/bin/python3
def print_list_integer(my_list=[])
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
    print("--")
    print_list_integer()
