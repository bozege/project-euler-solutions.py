#sum of even fibonacci numbers whose values do not exceed four million.

fib1 = 1
fib2 = 2
fib3 = fib1 + fib2

sum = 2

while fib3 <= 4000000:
    if fib3 % 2 == 0:
        sum += fib3
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
print(sum)
        
    