#!/usr/bin/python3
for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        str = 'fizzbuzz'
    else:
        if (i % 3 == 0):
            str = 'fizz'
        elif (i % 5 == 0):
            str = 'buzz'
        else:
            str = format(i)
    print("{}".format(str), end=" ")
