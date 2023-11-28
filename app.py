# write "Choose one of the elements (rock, paper, or scissors)" to the console and ask the user to choose one of the elements
# store the user's choice in a variable
# generate a random choice for the computer and store it in a variable
# write the computer's choice to the console
# write the result of the game to the console (e.g. "You won!" or "You lost!")
# if the user won, increase the number of wins by 1
# if the user lost, increase the number of losses by 1
# if the user tied, increase the number of ties by 1
# write the number of wins, losses, and ties to the console
# ask the user if they want to play again
# if the user says yes, start the game over
# if the user says no, end the game
# if the user enters something other than yes or no, ask the user again
# if the user enters something other than rock, paper, or scissors, inform the player if the option entered by the player is invalid and ask the user again
# if the user enters something other than yes or no, ask the user again
# when game ends, write "Thanks for playing!" to the console and inform the user of the number of wins, losses, ties, and rounds played
# Path: app.py


import random
import sys

print("Welcome to Rock, Paper, Scissors!")
print("Choose one of the elements (rock, paper, or scissors)")
print("Type exit to quit the game")

wins = 0
losses = 0
ties = 0
rounds = 0
choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Choose: ").lower()
    if user_choice == 'exit':
        sys.exit()
    elif user_choice not in choices:
        print("Invalid choice")
        print("Please choose rock, paper, or scissors")
        continue
    computer_choice = random.choice(choices)
    print("Computer chose: " + computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif user_choice == 'rock' and computer_choice == 'paper':
        print("You lost!")
        losses += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You won!")
        wins += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You won!")
        wins += 1
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print("You lost!")
        losses += 1
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print("You lost!")
        losses += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You won!")
        wins += 1
    rounds += 1
    print("Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties))
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'no':
        print("Thanks for playing!")
        print("Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties) + " Rounds Played: " + str(rounds))
        sys.exit()
    elif play_again == 'yes':
        continue
    else:
        print("Please enter yes or no")
        continue