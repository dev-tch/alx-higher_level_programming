#!/usr/bin/python3
def multiple_returns(sentence):
    size = 0
    first = None
    if sentence:
        first = sentence[0]
        size = len(sentence)
    new_tuple = (size, first)
    return (new_tuple)
