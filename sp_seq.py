import math
Length=int(input())
String=input()
garbage_count= String.count('?')
#print(garbage_count)
st_i=(Length//2)-1
en_i=(Length//2)
same=0
for iteration in range((Length-garbage_count)//2):
    if String[st_i]==String[en_i].upper():
        st_i-=1
        en_i+=1
        same=1



if same==1:
    print(int(math.pow(3,garbage_count//2)))
else:
    print(int(math.pow(3,((garbage_count//2)-1))))