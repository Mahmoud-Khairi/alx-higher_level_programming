#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        a = my_list[1]
        for index in range(0, len(my_list)):
            if my_list[index] > a:
                a = my_list[index]
        return a
    else:
        return None
