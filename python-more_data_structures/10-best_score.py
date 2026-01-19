#!/usr/bin/python3
def best_score(a_dictionary):
    best_value = 0
    best_key = ""
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > best_value:
                best_value = a_dictionary[key]
                best_key = key
    else:
        best_key = None
    return best_key
