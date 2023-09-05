#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ascii_ch = ord(ch)
        char = ch
        if (ascii_ch >= ord('a') and ascii_ch <= ord('z')):
            char = format(chr(ascii_ch - 32))
        print("{}".format(char), end="")
    print("")
