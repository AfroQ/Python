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
