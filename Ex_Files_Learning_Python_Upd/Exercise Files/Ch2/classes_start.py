#
# Example file for working with classes
# Sometimes functions are called methods
# Sometimes variables inside a class are called properties (But say class variables)
# The first argument for a method inside a class is always "self"
# "self" is a reference to the object when class is used to create an object
# This is inorder to reference the object itself, for example (c and donald below)

class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, something):
        print("myClass method2 " + something)

class anotherClass(myClass): #inheriting from myClass
    def method1(self):
        myClass.method1(self) #Calling the inherited class
        print("anotherClass method1") 

    def method2(self, something):
        print("anotherClass method2 ") #This overwrites the method2 above (the child has precedence)

class Duck:
    def quack(self):
        print("Quaack!")
    def walk (self):
        print("walks like a duck")

    #you can also give these variables within the class to get the same result
    #sound = 'Quaack!'
    #walking = 'walks like a duck'
    #def quack(self):
    #     print(self.sound)
    # def walk(self):
    #     print(self.walking)

def main():
    c = myClass() # c is an object of the class "myClass"
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string") #This argument will not be printed

    donald = Duck() # Donald is an object of the class "Duck"
    donald.quack() #quack and walk are members of the object donald
    donald.walk()

if __name__ == "__main__":
    main()

