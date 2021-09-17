print("How many programmers are there?")
programmers = int(input())

print("How many monkeys are there?")
monkeys = int(input())
# `we take in two variables from the user and convert them to integers.`
# `input takes in everything as a string but,` 
# `if we want to compare them as numbers, they have to be considered numbers.`
if monkeys > programmers:
  print("We have the works of Shakespeare.")
# `if not skip over and run the next test` 
elif monkeys < programmers:
  print("We have some dodgy code.")
# `if that doesn't fit the condition too, run the last test` 
else:
  print("The monkeys and programmers go to war.")
  name = 'Alice'
  if name == 'Alice':
    print('Hi Alice')