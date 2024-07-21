T=int(input())
res=[]
for case in range(T):
    n=int(input())
    s=input()
    List=[]
    for i in s:
        List.append(i)
    l=List.count('L')
    r=List.count('R')
    q=List.count('?')

    if l>=r:
        res.append((l+q)-r)
    elif r>l:
        res.append((r+q)-l)
for x in res:
    print(x)