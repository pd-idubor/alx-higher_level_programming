#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str[:])):
        if i == n:
            continue
        print("{}".format(str[i]), end="")
    return("")
