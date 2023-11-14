import random

def play_game(user_choice):
    choices = ["rock", "scissors", "paper"]
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win! Жизнь игра - играй красиво!"
    else:
        return "Computer wins!"


user_input = input("Enter your choice (rock/scissors/paper): ").lower()

if user_input in ["rock", "scissors", "paper"]:
    result = play_game(user_input)
    print(result)
else:
    print("Invalid choice. Please enter rock, scissors, or paper.")