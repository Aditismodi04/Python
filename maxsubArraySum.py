# this code gives maximum sum of array as output
def maxsubArray(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum = max(curr_sum+num,num)
        if(max_sum<curr_sum):
            max_sum = curr_sum
    return max_sum
def main():
    arr = [2,5,7,1,-2,3]
    result = maxsubArray(arr)
    print(result)       
main()  