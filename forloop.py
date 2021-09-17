import os
os.chdir("C:/Users/nyaku/OneDrive/Desktop/python")
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

total = 0
for num in range(101):
    total = total + num
print(total)


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
    

