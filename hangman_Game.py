import random
word = ["python","html","css","java","javascript","react"]
def choose_word():
    return random.choice(word)
def display_word(word,guess_letters):
    return" ".join(letter if letter in guess_letters else "_" for letter in word )
def hangman():
    print("\n** Welcome to the hangman game**")
    word = choose_word()
    guess_letters = set()
    max_attempts = 6
    wrong_attemps = set()
    
    while(len(wrong_attemps)<max_attempts):
        print("\nWord : ",display_word(word,guess_letters))
        print(f"attemps : '{len(wrong_attemps)}'/'{max_attempts}'")
        print(f"wrong letters : '{', '.join(wrong_attemps) if wrong_attemps else 'None'}'")
        
        guess = input("\nguess a letter of word: ")
        if(len(guess) != 1 or not guess.isalpha()):
            print("Invalid input")
            continue
        if guess in guess_letters:
            print("\nalredy gueesed")
        if guess in word:
            guess_letters.add(guess)
            print("Correct guess!!!")
        else:
            wrong_attemps.add(guess)
            print("wrong guess")
        if all(letter in guess_letters for letter in word):
            print("you won the game".upper())
            print("Word: " ,word.upper())
            play_again = input("\ntype yes if you want to play again : ")
            if(play_again == "yes"):
                    hangman()
            else:
                   exit()
    else:
        print("you lost!! the correct word was",word.upper())
        play_again = input("\ntype yes if you want to play again : ")
        if(play_again == "yes"):
                    hangman()
        else:
                  exit()
    exit
hangman()

