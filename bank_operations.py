balance = 0
def credit():
    try:
        global balance
        amount = int(input("\nenter the amouunt that you want to add to bank acount: \n"))
        balance = balance+amount
    except ValueError:
        print("please enter valid amount")    
def debit():
    try:
        global balance
        debit_amount = int(input("please enter the amount you want  to withdraw: \n"))
        balance = balance-debit_amount
    except ValueError:
        print("please enter valid amount")
def view_balance():
    global balance
    if(balance == 0):
        print("your balance is zero\n")
    else:
        print(f"\nBalance :'{balance}'\n")
def main():
    print("\n Welcome to the banking system ")
    print("-"*40)
    while True:
        print(" 1.add money\n" ,"2.withdraw money\n", "3.view balace\n", "4.exit")
        choice = int(input("please choice the number(1-4): \n"))
        if(choice == 1):
            credit()
            print("Balance added sucessfully\n")
        elif(choice == 2):
            debit()
            print("withdraw succesful\n")
        elif(choice == 3):
            view_balance()
        elif(choice == 4):
            print("\nThanks for visiting!!!!")
            exit()
        else:
            print("please enter valid number")
main()