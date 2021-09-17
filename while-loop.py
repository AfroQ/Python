spam = 0
while spam < 5:
    print('Hello')
    spam = spam + 1
#This is called iteration
#The difference with if is while loops back through the code


name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you!')

# Using break 
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

#using continue

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 2:
        continue
    print('spam is ' + str(spam))
