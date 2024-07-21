from string import *
s=input()
temp=None
r=[]
for i in range(len(s)):
    if s[i]!=temp:
        temp=s[i]
        r.append(s[i])
count=[]
for j in r:
    count.append(s.count(j))
print(r,count)
for y in count:
    y= str(y)
result=[]
for x in range(len(r)):
    result.append(r[x])
    result.append(count[x])

print(''.join(map(str,result)))