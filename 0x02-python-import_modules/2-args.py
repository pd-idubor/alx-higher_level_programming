#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args == 0:
        print("{} arguments.".format(args))

    elif args == 1:
        print("{} argument".format(args))
    else:
        print("{} arguments:".format(args))
    for x in range(1, args + 1):
        print("{}: {}".format(x, sys.argv[x]))
