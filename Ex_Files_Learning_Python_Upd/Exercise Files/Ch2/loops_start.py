#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
    print (x)
    x += 1

  #fibonnaci sequence
  a, b = 0, 1
  while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a+b
  
  print() #line ending 

  #password
  secret = 'swordfish'
  pw = ''
  auth = False
  count = 0
  max_attemt = 5
  while pw != secret:
    count += 1
    if count > max_attemt: 
      print("You have reached the maximum number of attempts")
      break
    else:
      auth = True
    pw = input(f"{count}: what is the secret word?")
    


  # define a for loop
  for x in range (5):
    print (x)
   # x += 1

  # use a for loop over an iterable collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # use the break and continue statements
  for x in range (5, 10):
    if (x == 7): break
    print (x) #the loop will stop once the condition is met (x == 7)
  
  for x in range (5, 10):
    if (x % 2 == 0): continue #Skips even numbers
    print (x)
  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate (days): # enumerate will return the index value
    print (i, d) 

if __name__ == "__main__":
  main()


#More practice 
def step(start, stop, step):
    for i in range(start, stop, step):
        print(i, end =' ')
step(50, 19, -2)

x = 50 
while x > 19:
    print(x, end= ' ')
    x = x - 2

# Reversed range

for i in reversed(range(0, 101, 2)):
  print (i, end=' ')

#Fizzbuzz challenge

for i in range(1, 101):
    x = ''
    if i % 4 == 0:
        x = 'Go'
      #  print(str(i) + 'Go', end= ' ')
    if i % 5 == 0:
        x = 'Figure'
      #  print(str(i) + 'Figure', end= ' ')
    if(i % 4 == 0 and i % 5 == 0):
        x = 'GoFigure' 
       # print("GoFigure", end =' ')

    print(x, end= ' ')

for i in range(1, 101):
    if(i % 4 == 0 and i % 5 == 0):
       print("GoFigure", end =' ')
       continue
    if i % 4 == 0:
       print('Go', end= ' ')
       continue
    if i % 5 == 0:
       print('Figure', end= ' ')
       continue

    #print(i, end= ' ') 

for i in range(1, 101):
    if(i % 4 == 0 and i % 5 == 0):
       print("GoFigure", end =' ')
       continue
    elif i % 4 == 0:
       print('Go', end= ' ')
       continue
    elif i % 5 == 0:
       print('Figure', end= ' ')
       continue

    #print(i, end= ' ') 

