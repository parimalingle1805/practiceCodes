def insertionSort(arr):
    Sorted=[arr.pop(0)]
    for i in range(0,len(arr)):
        Sorted.append(arr.pop(0))
        j=len(Sorted)-1
        while Sorted[j-1]>Sorted[j] and j>0:
            if Sorted[j-1]>Sorted[j]:
                Sorted[j-1],Sorted[j]=Sorted[j],Sorted[j-1]
            j-=1
    return Sorted
print(insertionSort([8,7,6,5,4,3,4,46,0]))