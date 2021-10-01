# Example file for working with functions

# define a basic function
def func1():
    print("this is a function")
func1() #prints
print(func1()) #prints the function, then tries to print the "print" function which evaluates to none
print(func1) #Does not print

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)
func2(10, 20)
# function that returns a value
def cube(x):
    return(x*x*x)
print(cube(5))
# function with default value for an argument
def power (num, x=1):
    result = 1
    for i in range (x):
        result = result * num
    return result

print (power(2))
print(power(2, 3))
#you can call the arguments in chosen order 

print(power(x=3, num=2))


#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
#The star  character means we can pass in any number of arguments which will be looped over and added to a running total
print(multi_add(2, 3, 9, 78))

def isprime(n):
    if n<=1:
        return False
    for x in range (2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range (100):
        if isprime(n):
            print(n, end=' ', flush=True)
list_primes()

def main():
    kitten()

def kitten():
    print("meow")
if __name__ == '__main__': main()