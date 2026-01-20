#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if isinstance(roman_string, str):
        for i in range(0, len(roman_string)-1):
            if roman_dict[roman_string[i]] >= roman_dict[roman_string[i+1]]:
                total += roman_dict[roman_string[i]]
            elif roman_dict[roman_string[i]] < roman_dict[roman_string[i+1]]:
                total -= roman_dict[roman_string[i]]
        total += roman_dict[roman_string[-1]]
    else:
        return 0
    return total
