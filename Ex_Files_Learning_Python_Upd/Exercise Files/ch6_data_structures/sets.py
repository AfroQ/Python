#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A set is a like a list that does not allow duplicate elements
def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a) # you can use sorted to make sure they come back in the same order each time
    print_set(b)

    # you can find members in one set not the other by doing (a - b)
    # ones in either or both (a | b)
    # look for the exclusive or (a ^ b)
    # Only members that are in both (a & b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
