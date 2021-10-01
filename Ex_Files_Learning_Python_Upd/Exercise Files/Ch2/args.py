#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')

#Another representation - printing pre-determined tuple
    x = ('quack', 'moo', 'roar', 'chirp')
    sounds(*x)


def kitten(*args): #This lets you enter moultiple arguments
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

#can also do...
def sounds(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')



if __name__ == '__main__': main()
