#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    nb_args = len(argv) - 1
    if (nb_args == 1):
        print(f"1 argument:")
        print(f"1: {argv[1]}")
    elif (nb_args == 0):
        print("0 arguments.")
    elif (nb_args > 1):
        print(f"{nb_args} arguments:")
        for i in range(1, nb_args + 1):
            print(f"{i}: {argv[i]}")
