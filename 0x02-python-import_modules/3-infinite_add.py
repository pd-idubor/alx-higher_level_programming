#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    args = len(sys.argv) - 1
    for x in range(1, args + 1):
        sum += int(sys.argv[x])
    print("{}".format(sum))
