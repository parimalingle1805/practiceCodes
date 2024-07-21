from math import *
from itertools import *
def collision(List1,List2):
    x1=List1[0]
    y1=List1[1]
    v1=List1[2]
    x2=List2[0]
    y2=List2[1]
    v2=List2[2]
    dist1=sqrt((x1*x1)+(y1*y1))
    dist2=sqrt((x2*x2)+(y2*y2))
    t1=dist1/v1
    t2=dist2/v2
    if t1==t2:
        return True
    else:
        return False



n=int(input())
coor_list=[]
for case in range(n):
    coordinates=list(map(int,input().split()))
    coor_list.append(coordinates)

start=0
other=1
count=0
for i in range(0,len(coor_list)-1,1):
    for j in range(i+1,len(coor_list),1):
        if collision(coor_list[i],coor_list[j])==True:
            count+=1
print(count)