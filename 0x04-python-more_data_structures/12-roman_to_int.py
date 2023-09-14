#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not roman_string.isalpha():
        return (0)
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    size = len(roman_string)
    next = ''
    current = ''
    str = roman_string
    for i in range(size):
        current = str[i]
        current_val = dict.get(current.upper(), 0)
        if (i + 1) < size:
            next = str[i + 1]
            next_val = dict.get(next.upper(), 0)
            if current_val < next_val:
                sum = sum - current_val
            else:
                sum = sum + current_val
        else:
            sum = sum + current_val
    return (sum)
