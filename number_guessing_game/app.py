
import random  # Importing the random module to generate random numbers

# Printing a welcome message explaining the game
print("Welcome to the game, this is a number guessing game! \nYou got 5 attempts to guess the number between 50 and 100 \nLet's start the game!")

# Generating a random number between 50 and 100 (inclusive of 100)
number_to_guess = random.randrange(50, 101)  # range should include 100, so we use 101

# Initializing the number of chances (attempts) the player has
chances = 5
# Counter for the number of guesses made by the player
guess_counter = 0

# Starting the loop to allow the player to make guesses
while guess_counter < chances:
    guess_counter += 1  # Increment the guess counter each time a new guess is made
    # Taking the player's guess as input and converting it to an integer
    my_guess = int(input("Please enter your guess: "))
    
    # Checking if the player's guess is correct
    if my_guess == number_to_guess:
        # If correct, print the success message and break out of the loop
        print(f"The number is {number_to_guess} and you found it right! in the {guess_counter} attempt")
        break
    # If the guess is too low, inform the player and let them try again
    elif my_guess < number_to_guess:
        print("Your guess is too low, try again!")
    # If the guess is too high, inform the player and let them try again
    elif my_guess > number_to_guess:
        print("Your guess is too high, try again!")
    
    # If the player has used all their chances without guessing correctly
    if guess_counter == chances:
        print(f"Oops sorry, the number is {number_to_guess}. Better luck next time!")
