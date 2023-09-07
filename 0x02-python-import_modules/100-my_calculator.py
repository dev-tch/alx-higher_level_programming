#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    from sys import exit
    operators = '+-*/'
    nb_args = len(argv) - 1
    if (nb_args != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ope = argv[2]
    if ope[0] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if (ope[0] == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    if (ope[0] == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if (ope[0] == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if (ope[0] == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
