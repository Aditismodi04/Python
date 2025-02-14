# this code gives second largest ekement of the array as output
def seconf_largest(arr):
    seconf_largest = largest_ele = float('-inf')
    n = len(arr)
    for num in arr:
        if(num>largest_ele):
            seconf_largest = largest_ele
            largest_ele = num
        elif(num>seconf_largest and num != largest_ele):
            seconf_largest = num
    return seconf_largest if num != float('-inf') else -1
def main():
    arr = [1,2,3,4,5]
    result = seconf_largest(arr)
    print(result)
main()              