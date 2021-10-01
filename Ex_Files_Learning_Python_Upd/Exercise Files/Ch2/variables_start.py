# 
# Example file for variables
#

# Declare a variable and initialize it
num = 0
print(num)


# re-declaring the variable works
num = 20
print(num)


# ERROR: variables of different types cannot be combined
#print("abc" + 123
print("abc" + str(123))

# Global vs. local variables in functions
num = "abc" #global variable
def func():
    num = 89 #local variable
    print(num)
func()
print(num)

#You can now specify that you want the program to interpret the num variable as global 
def func():
    global num #declaring num as global
    num = 89 #local variable
    print(num)
func()
print(num)
# 89 gets printed twice
# Assigning num inside the function a "global" value affects the num value outside of the function

# you can undefine variables in real time by using "del"
del num
print(num) #error message