def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0)) #this will return an error because computers are dump jk
print(div42by(1))

#modify with try and accept statements as seen above
#this can be used to catch all errors as below

def div42by(divideBy):
    try:
        return 42/divideBy
    except:
        print('Error')

print(div42by(2))
print(div42by(12))
print(div42by(0)) #this will return an error because computers are dump jk
print(div42by(1))
