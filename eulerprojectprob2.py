#sum of even fibonacci numbers below four million.

def fibonacci(n):
    
    fib1 = 1
    fib2 = 2
    fib3 = fib1 + fib2
    fiblist = [1,2]
    while fib3 < n:
        fiblist.extend([fib3])
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
    
    return(fiblist)

sum = 0
for i in range (0,len(fibonacci(4000000))):
    if fibonacci(4000000)[i] % 2 == 0:
        sum += fibonacci(4000000)[i]
print("Sum of all even fibonacci numbers until that number is: ", sum)
        
    
