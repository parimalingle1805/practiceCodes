import sys
sys.stdout=open('/Users/Parimal/PycharmProjects/p11/fb_A.txt','wt')

T=int(input())

for case in range(T):
    N=int(input())
    I_list=input()
    O_list=input()
    I=[]
    O=[]
    for i in I_list:
        I.append(i)
    for i in O_list:
        O.append(i)
    
    print("Case #",end="")
    print(case+1,end=":")
    print()
    
    for i in range(N):
        for j in range(N):
            if i==j:
                print('Y',end="")
            else:
                if (i-j==1 or j-i==1) and O[i]=='Y' and I[j]=='Y':
                    print('Y',end="")
                else:
                    if i<j and O[i]=='Y' and I[j]=='Y':
                        flag=True
                        for x in range(i+1,j,1):
                            if I[x]=='Y' and O[x]=='Y':
                                flag=True
                            else:
                                flag=False
                                break
                        if flag==True:
                            print('Y',end="")
                        else:
                            print('N',end="")
                    elif i>j and O[i]=='Y' and I[j]=='Y':
                        flag=True
                        for x in range(i-1,j,-1):
                            if I[x]=='Y' and O[x]=='Y':
                                flag=True
                            else:
                                flag=False
                                break
                        if flag==True:
                            print('Y',end="")
                        else:
                            print('N',end="")
                    else:
                        print('N',end="")
        print()
#File.close()