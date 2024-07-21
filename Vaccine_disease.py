T = int(input())
result_final=[]
for case in range(T):
    vaccine = list(map(int,input().split()))
    disease = list(map(int, input().split()))
    result=[]
    for x,y in vaccine,disease:
        if x>y:
            result.append('Yes')
        else:
            result.append('No')

    if result.count('No')>0:
        result_final.append('No')
    else:
        result_final.append('Yes')
for i in result_final:
    print(i)