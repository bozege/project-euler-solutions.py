#sum of all the mutliplies of 3 or 5 below 1000.

n =  3
sum = 0
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        sum += n
    n += 1
print(sum)