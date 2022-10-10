#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    len1 = len(my_list_1)
    len2 = len(my_list_2)
    new = []

    for i in range(list_length):
        res = 0

        try:
            res = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")

        except (TypeError, ValueError):
            print("wrong type")

        except IndexError:
            print("out of range")

        finally:
            new.append(res)
    return (new)
