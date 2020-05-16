#This program finds the only Pythogerian triplet's product for which a + b + c = 1000

for a in range (1,1000):
    for b in range (1,1000):
        if ((a**2 + b**2)**(1/2)) - int((a**2 + b**2)**(1/2)) == 0:
            c = int((a**2 + b**2)**(1/2))
            if a+b+c == 1000:
                product = a*b*c
                sum = a+b+c
                print("a =",a, "b = ",b, "c = ",c)
                print("The product is: ",product)
                break
                    
                
                
                


                                        
