# This is a list, it allows you to store multiple things 
# in one variable.
firefly = ["Mal", "Jayne", "Kaylee", "River", "Wash", 
"Zoe", "Simon", "Inara", "Book"]

# Now for the 'for' loop
for character in firefly:
  print("I think " + character + " is awesome!")

# Now for the while loop
firefly_fans = 0
while (firefly_fans < 1000):
  print("Firefly fans: " + str(firefly_fans))
  firefly_fans = firefly_fans + 1

print("Firefly is finally popular!")
# So while the number of firefly_fans is less than 1000, 
# keep running this code.
# If we forgot to add 1 to the number of firefly_fans, 
# the loop would keep going forever!

# Lists 
animals = ["cat", "dog", "wolf", "bear"]

# to get specific info, we use index positions
print(animals[0]) # prints cat

# Dictionaries - similar to lists 

person = {"name": "Bob", "age": 22}

print(person["name"])
print(person["age"])

#Before byte objects can be used as strings they must be decoded.

#To do this you can use the .decode() function on the object, for example:
byteobj = b'Hello World'
stringobj = byteobj.decode()
print(stringobj)

#Likewise to turn a string into a byte object it must be encoded 
#using the .encode() function on the object. For example:

stringobj = "Hello World"
byteobj = stringobj.encode()
print(byteobj)     