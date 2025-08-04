from abc import ABC, abstractmethod

# Abstract ATM Interface
class ATMinterface(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

# ATM Implementation
class ATM(ATMinterface):
    def __init__(self, atm_pin, balance):
        self.__atm_pin = atm_pin
        self.__balance = balance

    def pin_verify(self, pin):
        return self.__atm_pin == pin  # Fixed logic

    def check_balance(self):
        print("Your current balance is:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            print(amount, "Rs withdrawn from your account")
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.__balance += amount
        print(amount, "Rs deposited to your account")

# Main logic
def main():
    atm = ATM("1234", 50000)
    print("WELCOME TO ATM MACHINE")
    print("**************************")
    
    pin_input = input("ENTER YOUR ATM PIN: ")

    if atm.pin_verify(pin_input):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == "4":
                print("THANK YOU FOR VISITING")
                break
            else:
                print("Invalid choice")
    else:
        print("Incorrect PIN")

main()
