from itertools import *

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

def Fibonacci(n,a,b): 
    
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        print(a) 
    elif n == 1: 
        print(b) 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        print(b)  
  

def isprime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

n12=list(map(int,input().split()))
n1=n12[0]
n2=n12[1]
first_list=[]
for i in range(n1,n2,1):
    if isprime(i)==True:
        first_list.append(i)

comb_tup=combinations(first_list,2)
count=0
comb_list=[]
#print(comb_tup)
for k in comb_tup:
    a=str(k[0])
    b=str(k[1])
    c=int(a+b)
    d=int(b+a)
    comb_list.append(c)
    comb_list.append(d)
#print(comb_list)
second_list=[]
for l in comb_list:
    if isprime(l)==True:
        second_list.append(l)
#print(first_list)
#print(comb_list)
#print(second_list)
MAX=max(second_list)
MIN=min(second_list)
#print(MIN,MAX)
#FibArray = [MIN,MAX]
#print(len(second_list))
List=Remove(second_list)
#print(len(List))
Fibonacci(len(List),MIN,MAX)