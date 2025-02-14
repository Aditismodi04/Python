'''
a = int(input( 'enter any num:' ))
b= float(input("enter second num:"))
print(a+b)
'''

'''
input("college")
input("branch ")
(input("year and semester "))
int(input("enrollment no " )) 
'''

#wap to get a no from and check its odd or even
'''
num = int(input("enter any integer no: "))

if num%2==0:
    print("entered num is even")
    
else:
    print("entered num id odd")  
    '''
    
 #wap to find gretest of 3 number entered  user   
''' 
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
num3 = int(input("enter 3rd number: "))

if(num1>num2): 
    if(num1>num3):
        print(num1,"is highest")
    else:
        print(num3,"is highest")
else:
     print(num2,"is highest") 
     '''
     
 #wap to find number is multiple of seven or not
'''    
number = int(input("Enter any number: "))

if number%7==0:
    print(number,"is multiple of seven")
else:
    print(number,"is not multiple of seven")    
'''    
    #wap to ask user to enter their name and store it in list
'''
name_1 = input("enter your name: ")  
surname = input("enter your surname: ")      
last_name = input("enter your last name: ")  
list = [name_1,surname,last_name]    
print(list)
'''
#wap to check our list is plalindrome or not
'''
List = [1,2,3,2,1]
copy = List.copy()

reverse = List.reverse()
print(List)
if(copy==List):
    print("List is palindrome")
else:
    print("List is not palindrome")        
'''   
Grade = ["A","C","D","A","B","A"]
print(Grade.count("A"))
print(Grade.sort()) 
print(Grade)