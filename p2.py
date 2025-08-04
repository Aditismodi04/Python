def  revArr(arr):
    n = len(arr)
    j = n-1
    i = 0
    while i<=j:
        arr[i] , arr[j] = arr[j] ,arr[i]
        j-=1
        i+=1
    return arr
arr = [1,2,3,4]
print(revArr(arr))