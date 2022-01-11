import sys
from typing import Type # Gives more information about an error 
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
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
        yield i
        i += step
def main():
    try:
        x= 5/0
        y=int("foo") #wil return a ValueError
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('Don\'t divide by zero')
    except:
        print(f'Unkown error: {sys.exec_info()[1]}') #Returns the specific error
    else:
        print('There were no errors!')
    
    try:
        for i in inclusive_range(25): # will take between 1 and 3 arguments and return error if more or less
         print(i, end = ' ', flush = True)
    except TypeError as e:
        print(f'range error: {e}')
        
    print()

if __name__ == '__main__':main()