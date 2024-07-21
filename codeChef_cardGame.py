def Sum(s):
    sumOfDigits=0
    for i in s:
        sumOfDigits+=int(i)
    return sumOfDigits


T=int(input())

for case in range(T):
    chef=0
    morty=0
    turns=int(input())
    for turn in range(turns):
        In=list(map(str,input().split()))
        if Sum(In[0])>Sum(In[1]):
            chef+=1
        elif Sum(In[0])==Sum(In[1]):
            chef+=1
            morty+=1
        else:
            morty+=1
    if chef>morty:
        print(0,chef)
    elif morty>chef:
        print(1,morty)
    else:
        print(2,chef)