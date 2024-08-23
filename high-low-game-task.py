import random


def play_high_low_game(rounds=5):
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0
    
    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}")
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()

        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")

    print("Thanks for playing!")
    if score == rounds:
        print("Wow! You played perfectly!")
    elif score >= rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    

# Start the game
play_high_low_game()
