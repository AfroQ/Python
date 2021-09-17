If Statements

**If** - conditional 

- An if statement can be used to conditionally execute code, depending on whether the "if" statement's condition is True or False.

**elif** - if previous evaluation was FALSE, THEN this condition is evaluated (new condition)

- An elif (that is, "else if") statement can follow an if statement. Its block executes if its condition is True and all the previous conditions have been False.

**else** - if previous evaluation was FALSE, THEN this line is take (no new conditional being evaluated)

- An else statement comes at the end. Its block is executed if all of the previous conditions have been False.
  

```python
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

#Another example
name = 'Bob'
if name == 'Alice':
    print('Hi Alice')
else:
    print('not Alice')
print('Done')

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('woah')
else:
    print('no Alice here')
```

The values 0 (integer), 0.0 (float), and ‘‘ (the empty string) are considered to be "falsey" values. When used in conditions they are considered False. You can always see for yourself which values are truthy or falsey by passing them to the bool() function.

```python
print('Enter a name')
name = input()
if name: 
    print('Thank you for entering a name')
else:
    print('you did not enter a name')
#if you do not enter a name, the empty string will be considered 'falsey' and the next condition will be executed
```

