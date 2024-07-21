def mergeSort(arr):
    if len(arr)>1:
        m=len(arr)//2
        left=arr[:m]
        right=arr[m:]

        left=mergeSort(left)
        right=mergeSort(right)

        arr=[]

        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)
    return arr

n=int(input())
arr=list(map(int,input().split()))
res=mergeSort(arr)
for x in res:
    print(x)
