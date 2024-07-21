from math import *

def prime(num):
    if num > 1: 
      
   # Iterate from 2 to n / 2  
        for i in range(2, num): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
            if (num % i) == 0: 
                return False 
                break
        else: 
            return True 
  
    else: 
        return False



T=int(input())
for case in range(T):
    c=int(input())
    n=0
    while n<10:
        sol_1=((2*n+1)+sqrt((2*n+1)**2-(4*c)))/2 
        print(sol_1)
        sol_2=((2*n+1)-sqrt((2*n+1)**2-(4*c)))/2
        print(sol)
        if prime(sol_1)==True and prime(sol_2)==True:
            print("Valid")
        else:
            print("Invalid")