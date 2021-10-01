#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A list comprehension is a list created based on another list or iterator.

def main():
    seq = range(11)
    seq2 = [x *2 for x in seq] # multiplies each item in seq by 2
    seq2 = [x for x in seq if x % 3 != 0] # each item not divisible by 3
    seq2 = [(x, x**2) for x in seq] # list of tuples, original element and squared

    #you can call functions
    from math import pi
    seq2 = [(x, x*pi) for x in seq]
    seq2 = [round(pi, x) for x in seq]

    #create a dictionary
    seq2 = { x: x**2 for x in seq }
    
    print_list(seq)
    print_dict(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}', end = ' ')
    print()


if __name__ == '__main__': main()
