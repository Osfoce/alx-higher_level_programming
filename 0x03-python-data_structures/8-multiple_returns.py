#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    if length == 0:
        my_tuple = 0, None
    else:
        first_string = sentence[0]
        my_tuple = length, first_string
    return length, first_string
