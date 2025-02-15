def add(num1,num2):
    addition = num1+num2
    print("Addition: ",addition)
def sub(num1,num2):
    subtraction = num1-num2
    print("subtraction: ",subtraction)
def div(num1,num2):
    try:
        division = num1/num2
        print("division: ",division)
    except ZeroDivisionError:
        print("can't divide by zero" )
def mul(num1,num2):
        multiplication = num1*num2
        print("multiplicaton: ",multiplication)

def modulo(num1,num2):
    try:
        modulo = num1%num2
        print("modulo: ",modulo)
    except ZeroDivisionError:
        print("please enter valid number")
def main():
    while True:
        num1 = int(input("enter number 1 : "))
        num2 = int(input("enter number 2 : "))
        add(num1,num2)
        sub(num1,num2)
        mul(num1,num2)
        div(num1,num2)
        modulo(num1,num2)
        break
        # print("1.addition")
        # print("2.subtraction")
        # print("3.division")
        # print("4.multiplication")
        # print("5.modulo")
        # print("6.exit")
        # choice = int(input("enter number for opertaion(1-6): ")) 
        # if(choice == 1):
        #     add(num1,num2)
        # elif(choice == 2):
        #     sub(num1,num2)
        # elif(choice == 3):
        #     div(num1,num2)
        # elif(choice == 4):
        #     mul(num1,num2)
        # elif(choice == 5):
        #     modulo(num1,num2)
        # elif(choice == 6):
        #     exit()
        # else:
        #     print("please enter valid number") 
        #     break  
main()