

T=int(input())
for case in range(T):
    N,K,W=map(int,input().split())
    L=list(map(int,input().split()))
    AL,BL,CL,DL=map(int,input().split())
    H= list(map(int, input().split()))
    AH,BH,CH,DH = map(int, input().split())
    P=[]
    if N>K:
        for i in range(K,N):
            L.append(((AL * L[i - 2] + BL * L[i - 1] + CL) % DL) + 1)
            H.append(((AH * H[i - 2] + BH * H[i - 1] + CH) % DH) + 1)
    flag1=True
    perimeter=0
    x0 = L[0]
    y0 = 0
    x1 = L[0] + W
    y1 = H[0]
    perimeter+=(2*((x1-x0)+(y1-y0)))
    P.append(perimeter)
    for i in range(1,N):

        if L[i]<=(L[i-1]+W) and flag1==True:
            x0=L[0]
            x1=L[i]+W
            y1=H[i]
            h=H[i]-H[i-1]
            if h<0:
                h*=-1
            perimeter=(2*((x1-x0)+(y1-y0))+(2*h))
            P.append(perimeter)

        elif L[i]<=(L[i-1]+W) and flag1==False:
            perimeter-=fal_perim
            x0=L[i-1]
            x1=L[i]+W
            y1=H[i]
            h = H[i] - H[i - 1]
            if h < 0:
                h *= -1
            perimeter += (2 * ((x1 - x0) + (y1 - y0)) + (2 * h))
            P.append(perimeter)
            fal_perim=(2 * ((x1 - x0) + (y1 - y0)) + (2 * h))

        else:
            flag=False
            x0=L[i]
            x1=L[i]+W
            y1=H[i]
            fal_perim=(2*((x1-x0)+(y1-y0)))
            perimeter+=(2*((x1-x0)+(y1-y0)))
            P.append(perimeter)
    product=1
    for peri in P:
        product*=peri
    print(product%1000000007)