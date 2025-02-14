# this code gives missing element from 1 to n in the array as a output.
def missingNumber(arr):
    n =len(arr)+1
    arr_sum = sum(arr)
    total_sum = int((n*(n+1))/2)
    missingNumber = total_sum - arr_sum
    return missingNumber
def main():
    arr = [1,2,3,7,5,6]
    result = missingNumber(arr)
    print(result)
main()    