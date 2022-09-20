#!/usr/bin/python3
for x in range(10):
    for n in range(10):
        if n < x or n == x:
            continue
        if x == 8 and n == 9:
            break
        print("{}{}".format(x, n), end=", ")
print("{}{}".format(x - 1, n))
