#sum of the squares of the numbers between given parameters.

def sumofsquares(a,b):
    sum = 0
    for i in range (a,b+1):
        sum += i**2
    
    return(sum)

#sum of the given numbers squared.

def squareofsum(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    return(sum**2)

a = 0
b = 0
while a == 0:
    a = int(input("Enter the first parameter: "))
while b == 0:
    b = int(input("Enter the second parameter: "))
if b < a:
    c = a
    a = b
    b = c    

result = squareofsum(a,b)-sumofsquares(a,b)
print("The difference is: ", result)