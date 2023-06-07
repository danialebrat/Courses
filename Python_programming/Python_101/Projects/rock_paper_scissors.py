import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if player_choice == "q":
            print("Thank you for playing!")
            break
        elif player_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        print(winner)

        if "You win" in winner:
            player_wins += 1
        elif "Computer wins" in winner:
            computer_wins += 1

        print(f"Player: {player_wins} | Computer: {computer_wins}\n")

        if player_wins == 3:
            print("Congratulations! You are the winner!")
            break
        elif computer_wins == 3:
            print("The computer is the winner!")
            break

# Start the game
play_game()
