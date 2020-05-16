#This function returns sum of all the primes which are below the given limit
def primelist(n):
    j = 0
    sum = 0
    if n == 2:
        sum = 0
    elif n == 3:
        sum +=2
    elif n >= 4:
        sum += 5
    
        
    for i in range (5,n,2):
        sqrt = int(i**(1/2))
        for j in range (2,sqrt+1):
            if i % j == 0:
                break
        if i % j != 0:
            sum += i
            
    return sum 

print("Sum of all the primes below that number is: ", primelist(2000000))
    


