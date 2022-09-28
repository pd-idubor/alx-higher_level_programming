#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str or roman_string is None):
        return (0)

    rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    num = 0

    for i, char in enumerate(roman_string):
        tmp = rom_dict[char]
        try:
            if tmp < rom_dict[roman_string[i + 1]]:
                tmp = tmp * -1
        except IndexError:
            pass
        num = num + tmp
    return (num)
