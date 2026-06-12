import random

def main():
    print("-" * 100)
    print("Welcome to the Number Guessing Game")
    print("\nIntro:")
    print(" -   1. Guess a number between 1-100")
    print(" -   2. You will have a certain amount of guesses depending on the difficulty you choose")
    print(" -   3. You will get hints as you keep guessing")
    print("-" * 100)
    
    dif ={
        "easy": 10, "medium": 5, "hard": 3
        }
    
    while True:
        level = input("Which difficulty would you like to attempt: easy, medium or hard: ").strip().lower()
        if level in dif:
            chances = dif[level]
            break
        print("Invalid answer, please try again")

    
    ran = random.randint(1,100)
    attempts = 0

    print(f"\nYou have have chosen difficulty: {chances}, you have {chances} attempts to guess the number, may the odds be in your favor!\n")
    
    while attempts < chances:
        
        try: 
            guess = int(input("What would you like to guess: ")) 
        except ValueError:
            print("Invalid reponse, please do a number")
            continue 
        if guess < 1 or guess > 100:
            print("Your number is out of range!")
            continue


        attempts += 1
        
        if guess == ran:
            print("You Won!")
        elif guess < ran:
            print("Your guess was too low")
        elif guess > ran:
            print("Your guess was too high")
        print(f"Remaining guesses left: {chances-attempts}")


        if attempts == chances - 1:
            print("You have 1 attempt left. Better make this one count")   
    else:
        print(f"You ran out of attempts! The number was: {ran})")

    while True:
        play_again = input("Would you like to play again\nYes or No (y/n): ").strip().lower()
        if play_again == "y":
            main()
        elif play_again == "n":
            break
            print("Thank you for playing!")
        else:
            print("Invalid resposne, respond with either \"y\" or \"n\"")
    





if __name__ == "__main__":
    main()