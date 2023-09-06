#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    str_res = ''
    for ch in str:
        if (index != n):
            str_res += ch
        index += 1
    return str_res
