#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A generator is a special class of function that serves as an iterator 
# instead of returning a single value the generator returns a stream of values.

def main():
    for i in inclusive_range(25): #returns values up to 25
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    # These are exceptetions to ame sure we provide arguments to the inclusive_range function
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i #yield is like a return but for generator
        i += step

if __name__ == '__main__': main()
