# Import the random module to simulate dice rolls
import random

# Define a function to simulate rolling a six-sided dice
def roll_dice():
    # Calls what side the dice rolls on, can be 1-6
    return random.randint(1, 6)

# Define a function to play one round of the game
def play_round(player1_roll, player2_roll):
    # Displays what each player rolls for that round
    print(f"Player 1 rolls a {player1_roll}, Player 2 rolls a {player2_roll}.")
    # If player 1 rolls higher than player 2, display a win for them
    if player1_roll > player2_roll:
        print("Player 1 wins the round.")
        # Return round result
        return "Player 1"
    # If player 2 rolls higher than player 1, display a win for them
    elif player2_roll > player1_roll:
        print("Player 2 wins the round.")
        # Return round result
        return "Player 2"
    # If both players roll the same, display a tie
    else:
        print("The round is a tie.")
        # Return round result
        return "Tie"

# Define a main function to orchestrate the dice rolling game
def main():
    # Ask the user for the number of rounds to play, check for errors
    while True:
        try:
            rounds = int(input("\nHow many rounds do you want to play? "))
            if rounds <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                break  # For a valid input, break the loop
        except ValueError:
            print("Please enter a whole number.")

    # Define counters for wins and ties
    player1_wins = 0
    player2_wins = 0
    ties = 0

    # Loop through the number of rounds
    for _ in range(rounds):
        # Roll the dice for both players
        player1 = roll_dice()
        player2 = roll_dice()

        # Determine the outcome of the round with result
        result = play_round(player1, player2)

        # Update win/tie counters, pull from returned result
        if result == "Player 1":
            player1_wins += 1
        elif result == "Player 2":
            player2_wins += 1
        else:
            ties += 1

    # Print the final score (wins/losses/ties)
    print(f"\nFinal Score: Player 1 wins {player1_wins} round(s). Player 2 wins {player2_wins} round(s). {ties} round(s) ended in a tie.")

    # Announce the overall winner or a tie
    if player1_wins > player2_wins:
        print("Overall Winner: Player 1!")
    elif player2_wins > player1_wins:
        print("Overall Winner: Player 2!")
    else:
        print("The game is a tie!")

# Call the main function to run the program
if __name__ == "__main__":
    main()
