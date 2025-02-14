# this code gives output as starting index and ending index 
# for subarray that gives sum of given target
def subarray(arr,target):
    n=len(arr)
    p2 = 0
    curr_sum = 0
    
    for p1 in range(n):
        curr_sum = curr_sum + arr[p1]
        
        while(curr_sum>target and p2<p1):
            curr_sum = curr_sum - arr[p2]
            p2 = p2+1
        if(curr_sum == target):
            return[p2+1,p1+1]  
    return [-1]     
def main():
    arr = [31, 21, 51, 11, 8]
    target = 52
    result= subarray(arr,target)
    print(result)
main()    
            
           