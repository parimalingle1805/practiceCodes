mn = list(map(int,input().split()))
m=mn[0]
n=mn[1]
temp=n//2
upper_triangle=2
lower_triangle=((m//2)*3)-1
for i in range(m):
    for j in range(n):
        if i==m//2:
            if j==((n//2)-3):
                print("WELCOME",end="")
            elif j>((n//2)-3) and j<((n//2)+4):
                print("",end="")
            else:
                print("-",end="")

        elif j>(temp-upper_triangle) and j<(temp+upper_triangle) and i<m//2:
            if j%3==0:
                print(".|.",end="")
            else:
                print("",end="")
        elif j>(temp-lower_triangle) and j<(temp+lower_triangle) and i>m//2:
            if j%3==0:
                print(".|.",end="")
            else:
                print("",end="")
        else:
            print("-",end="")
    upper_triangle+=3
    if i>m//2:
        lower_triangle-=3
    print()