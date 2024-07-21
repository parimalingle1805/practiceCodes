from itertools import *
from math import *

def Check(tup,arr1,arr2):
    X=0
    Y=0
    i=tup[0]
    j=tup[1]
    L=(tup[1]-tup[0])+1
    while i<=j:
        X+=arr1[i-1]
        i+=1
    i=tup[0]
    j=tup[1]
    while i<=j:
        Y+=arr2[i-1]
        i+=1
    #print(X,Y)
    if pow(X,Y)<=L and X!=2 and Y!=2:
        #print("True")
        return True
    else:
        #print("False")
        return False


N=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
l=1
List=[]
res=[]
while l<=N:
    List.append(l)
    l+=1
#print(List)
comb=combinations_with_replacement(List,2)
for i in comb:
    #print(i)
    if Check(i,arr1,arr2)==True:
        res.append(1)
print(len(res))