import sys
sys.stdout=open(r'C:\Users\Parimal\Downloads\FB_A2.txt','wt')    #To write output in a txt file
def dFirst(A, B, C):
    d = C // B
    C = C % B
    s = C // A
    bunsAvailable = (s + d) * 2
    pattiesAvailable = s + (d * 2)
    if pattiesAvailable == 0:
        return 0
    else:
        if bunsAvailable > pattiesAvailable:
            return  pattiesAvailable
        else:
            return bunsAvailable - 1

def sFirst(A, B, C):
    s = C // A
    C = C % A
    d = C // B
    bunsAvailable = (s + d) * 2
    pattiesAvailable = s + (d * 2)
    if pattiesAvailable == 0:
        return 0
    else:
        if bunsAvailable > pattiesAvailable:
            return pattiesAvailable
        else:
            return bunsAvailable - 1

for case in range(int(input())):
    A, B, C = map(int, input().split())
    res = max(dFirst(A, B, C), sFirst(A, B, C))
    #print(dFirst(A,B,C), sFirst(A, B, C))
    print(f'Case #{case + 1}: {res}')