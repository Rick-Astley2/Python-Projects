import random

def main():
    number = random.randint(1, 100)
    turns = 0

    
    while True:
        try:
            user_input = input("Guess a number between 1 and 100: ")
            user_input = int(user_input)
            
            if user_input > number:
                print("lower")
            elif user_input < number:
                print("higher")
            elif user_input == number:
                print(f"you got it, it took you {turns} guesses")
                break
        except ValueError:
            print("Please enter a valid number.")
        turns += 1

if __name__ == "__main__":
    main()