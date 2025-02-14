#a = int(input( 'enter any num:' ))
#b= float(input("enter second num:"))
#print(a+b)

def arrMax(arr , n):
    max = arr[0]
    n = len(arr)
    for i in range(1,n):
      if(arr[i] > max):
          max = arr[i]
    return max
def main():
    arr = [23,67,1,23,89]
    n = len(arr)
    print(arrMax(arr ,n))  
if __name__ == "__main__":
    main()   