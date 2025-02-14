import random

def randomNumber_guess():
    attemt = 0
    random_number = random.randint(1,50)
    print("\nwelcome to the random number guessing game")
    print("--------------------------------------------")
    try:
        while True:
        
                number = int(input("guess the number between 1 to 50: \n"))
                attemt+=1
                if(number>random_number):
                    print("\nyour number is greater than random number")
                elif(number<random_number):
                    print("\nyour number is lesser than random number")    
                else:
                    print(f"\nCongratulations!!!! you have guessed correct number in '{attemt}' attempt and  the number was '{random_number}'")
                    break
    except ValueError:
        print("please enter valid number!!!!")   

while True:
        randomNumber_guess()
        print("\ntype yes if you want to play again" )
        choice = input("do you want to play again? \n").lower()
        if(choice!="yes"):
            print("\nThanks for playing this game")
            break
            


    