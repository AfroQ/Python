#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Lists are mutable
# Uses square brackets

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game)
    print(game[2]) #prints item in the index 2 in the list
    print(game[1:5:2])  #prints specific items in the range, every second item
    
    # You can search for an item using the index function
    i = game.index('Paper')
    print([i])

    # You can add to the list
    game.append('Computer') #adds computer to the end of the list

    # Using "insert" -- You can specify the location to add an item
    game.insert(1, 'Smash')
    print_list(game)

    # You can remove an item by value
    game.remove('Paper')
    print_list(game)

    #pop removes item from end of the list or on a specific index
    game.pop()
    print_list(game)
    #you can also use del 

    # You can join a list
    print(', '.join(game)) #prints the list joined by comma space
    print_list(game)

    # Use the len function to get the raw length of the string
    print(len(game))
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
