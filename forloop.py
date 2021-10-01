#A "for" loop will loop a specific number of times.
#The range() function can be called with one, two, or three arguments.
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

# Adding all numbers between 1 and a hundred
total = 0
for num in range(101):
    total = total + num
print(total)

# You can also use a while loop 
num = 0
total = 0
while num < 100:
    num = num + 1
    total = total + num
print(str(total))

# Using steps
print('my name is ')
for i in range(5, -1, -1):
    print('Jimmy Five Times ' + str(i))
    