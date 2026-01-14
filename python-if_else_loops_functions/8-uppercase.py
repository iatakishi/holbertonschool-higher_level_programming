#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97:
            print(chr(ord(i) - 32), end = "")
        else:
            print(i, end = "")
    print()
