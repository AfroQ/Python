#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#Uses {} and has key value pairs separated by commas

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)
    
    # you can also do
    for k, v in animals.items():
        print(f'{k}: {v}')

# The keys argument provides a list of keys
    for k in animals.keys(): print(k)
# You can replace keys with values to get the values

# A dict is indexed by the key so you can do...
    print(animals['dragon']) #prints out the value
# You can the use this indexing style to add items to the dictionary as you do with lists 

    animals['monkey'] = 'haha'
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')
    # you can also do
    #for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
