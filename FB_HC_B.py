import sys
sys.stdout=open('/Users/Parimal/PycharmProjects/p11/fb_B.txt','wt')

T=int(input())
for case in range(T):
    n=int(input())
    s=input()
    #s=[]
    #for i in String:
    #    s.append(i)
    
    print("Case #",end="")
    print(case+1,end=": ")
    
    #if s=="AAA" or s=="BBB":
    #    print('N')

    #else:
    i=0
    flag=0
    while n>2:
        temp=s[i:i+3]
        if len(temp)<3:
            print('N')
            break
        elif temp=="AAA" or temp=="BBB":
            flag+=1
            if len(temp)<len(s) and len(temp)==3:
                i+=1
                continue
            else:
                print('N')
                break

        elif temp=="AAB" or temp=="ABA" or temp=="BAA":
            s=s[:i]+'A'+s[i+3:]
            n-=2
            i=0
        elif temp=="BBA" or temp=="BAB" or temp=="ABB":
            s = s[:i] + 'B' + s[i + 3:]
            n-=2
            i=0
    if n==1:
            print('Y')
