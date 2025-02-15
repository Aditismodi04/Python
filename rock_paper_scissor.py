import random
def computer_choice():
    comp = random.choice(["rock","paper","scissor"])
    return comp
def winner(user ,comp):
    if(user == "rock" and comp == "scissor") or (user == "paper" and comp == "rock") or (user == "scissor" and comp == "paper"):
        print("you winnnn!!!!!\n")
    elif(user == comp):
        print("draw!!!!!\n")
    else:
        print("you loseeee!!!!")
       
def main():
    print("Welcome to the rock paper scissor game")
    print("*" * 40)
    while True:
        user = input("\nenter your choice from rock paper scissor or write exit to quit: ")
        if(user == "exit"):
            print("Thanks for playing")
            break
        elif(user not in["rock","paper","scissor"]):
            print("enter valid choice")
       
        comp =  computer_choice()  
        winner(user,comp)
        print(f"\ncomputer choice: '{comp}'")
       
      
        
main()

