def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()
    left=[]
    right=[]
    for i in arr:
        if i<=pivot:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left)+[pivot]+quickSort(right)
    
arr=[1,6,7,9,4,3]
print(quickSort(arr))
