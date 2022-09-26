#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return(0, "None")
    for i in sentence:
        return(len(sentence), i)
