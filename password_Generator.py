import random
import string

def get_password(length):
     letters = string.ascii_letters 
     numbers = string.digits
     symbols = string.punctuation
     
     all_char = (letters+numbers+symbols)
     password = (random.choice(letters)+random.choice(numbers)+random.choice(symbols))
     password = password+''.join(random.choices(all_char,k=length-3))
     password = ''.join(random.sample(password,len(password)))
     return password
def main():
    while True:
     print("\n*** PASSWORD GENERATOR ***")
     length = int(input("\nEnter the length of password: "))
     if(length<4):
         print("please enter the length greater than 4 to create strong password: ")
         again = input("type yes to generate password again: \n").lower()
         if(again == "yes"):
             get_password(length)
             print("\nPassword : ",password)
             continue
         else:
             exit()
     else:
         password = get_password(length)
         print(f"\nPassword: '{password}'")
         again = input("type yes to generate password again: \n").lower()
         if(again == "yes"):
             get_password(length)
             print("\nPassword : ",password)
             continue
         else:
             exit()
     
main()
     