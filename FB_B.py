# import sys
# sys.stdout=open(r'C:\Users\Parimal\Downloads\FB_B.txt','wt')

def wins(r, c, a, b):
    if r == 2 and c == 2:
        return "NO"


for  case in range(int(input())):
    r, c, a, b = map(int, input().split())
