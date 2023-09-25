#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        nb = 0
        for item in my_list:
            if nb < x:
                print(item, end='')
                nb += 1
        print()
        return nb
    except Exception:
        return 0
