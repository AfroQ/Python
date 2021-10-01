# Example file for HelloWorld
print("Hello World!")
name = input("What is your name?")
print("Nice to meet you " + name)

def main():
    print("Hello World!")
    name = input("What is your name?")
    print("Nice to meet you " + name)
if __name__ == "_main_":
    main()

#using the .format method for place holder
x = 42
print('Hello world. {}'.format(x))

#we can also use the f string ...
x = 42
print(f'Hello world. {x}')

# this works like the %d %s formarts
x = 42
print("Hello world. %d" %(x)) #this method will be depracated