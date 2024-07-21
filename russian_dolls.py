n=int(input())
sz=[]
for IN in range(n):
    In=int(input())
    sz.append(In)
s=sorted(sz)
i=0
End=n-2
count=0
while len(s)>2:
    if s[0]<s[1]<s[2]:
        count+=1
        s.remove(s[0])
        s.remove(s[0])
        s.remove(s[0])
        #End-=3
        #i=0
print(count)
