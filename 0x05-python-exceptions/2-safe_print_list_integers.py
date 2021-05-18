#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counts = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            ++counts
        except (TypeError, ValueError):
            continue
    print("")
    return counts