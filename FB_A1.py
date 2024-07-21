import sys
sys.stdout=open(r'C:\Users\Parimal\Downloads\FB_A1.txt','wt')    #To write output in a txt file

for case in range(int(input())):
    s, d, k = map(int, input().split())
    bunsAvailable = (s + d) * 2
    pattiesAvailable = s + (d * 2)

    if pattiesAvailable >= k and bunsAvailable >= k + 1:
        print(f'Case #{case + 1}: YES')
    else:
        print(f'Case #{case + 1}: NO')
