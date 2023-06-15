#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    Integers = 0
    Rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    elements = [Rom_num.get(x) for x in roman_string]
    for idx, numeral in enumerate(elements):
        if(idx < len(elements) - 1):
            if elements[idx + 1] > numeral:
                Integers -= numeral
            else:
                Integers += numeral
        else:
            Integers += numeral
    return(Integers)
