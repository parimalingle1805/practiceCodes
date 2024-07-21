def countingSort(arr):
    Count=[0]*100
    result=[]
    for i in arr:
        Count[i]+=1
    for i in range(len(Count)):
        for j in range(Count[i]):
            result.append(i)
    return result
print(countingSort([1,1,3,2,1]))