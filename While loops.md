**While loops**

When the execution reaches the end of a "while" statement's block, it jumps back to the start to re-check the condition.

```python
spam = 0
while spam < 5:
    print('Hello')
    spam = spam + 1
#This is called iteration
#The difference with if is while loops loop back through the code
```

**Input validation**

```python
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you!')
```

**Infinite loops**

- sometimes you may have loops that do not have an escape condition. 

- ```python
  while True:
      print('Hello')
  ```

- You can press ctrl-c to interrupt an infinite loop. This hotkey stops Python programs.

**Break Statement** 

- A "break" statement causes the execution to immediately leave the loop, without re-check the condition.

```python
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
```

**Continue statement**

A "continue" statement causes the execution to immediate jump back to the start of the loop and re-check the condition.

```python
pam = 0
while spam < 5:
    spam = spam + 1
    if spam == 2:
        continue
    print('spam is ' + str(spam))
#Here the program will not print "spam is 2", because of the if statement that makes the program go back to the while loop
```

