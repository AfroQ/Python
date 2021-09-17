`with open('demo.txt') as file:`
  `print(file.read())`
# `Watch out for the tab before print!`

`def makeCapitals(arg1): #define function that takes one argument arg1`
  `caps = arg1.upper() # make a new variable assign it to the value of arg1 after it is uppercased`
  `return caps`
# `'Return' tells the program to go back to where you were in the code` 
# `when the function was called.`

`result = makeCapitals("hello, world!")`
`#we're calling makeCapitals and passing it a string.` 
`#That makes the code jump up to the function and arg1 then equals the string that was passed to it.` 
`#So arg1 would equal "hello, world!".`
`print(result)`