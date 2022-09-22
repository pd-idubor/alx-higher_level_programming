#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    if len(args) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    opr = args[2]
    b = int(args[3])

    if opr == '+':
        print("{} {} {} = {}".format(a, opr, b, add(a, b)))
    elif opr == '-':
        print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
    elif opr == '*':
        print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
    elif opr == '/':
        print("{} {} {} = {}".format(a, opr, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
