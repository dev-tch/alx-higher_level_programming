#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    len = len(argv) - 1
    for index in range(1, len + 1):
        sum = sum + int(argv[index])
    print(sum)
