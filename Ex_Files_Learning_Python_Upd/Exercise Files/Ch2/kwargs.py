#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Key word arguments are like list arguments that are dictionaries instead of tuples.
# This allows your function to have a variable number of named arguments.

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    # This is the same syntax as we use in dictionaries
    # you could also do...
    # x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    # kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
