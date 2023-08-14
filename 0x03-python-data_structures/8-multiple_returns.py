#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence[0] == 0:
        return None
    else:
        first_string = sentence[0]
    return length, first_string

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

