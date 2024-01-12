import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Main game loop
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if user_choice in ['rock', 'paper', 'scissors']:
        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
    elif user_choice == 'quit':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'quit'.")

