import random

def choose_word():
    # Add a list of words from which one will be chosen randomly
    word_list = ["python", "hangman", "programming", "computer","google",
    "coding"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with guessed letters and blanks for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    print("start your Guesses")
    # Choose a word for the player to guess
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(secret_word, guessed_letters)
        print("Word:", current_display)

        # Take a guess from the player
        guess = input("Enter a letter: ").lower()

        # Check if the guessed letter is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in secret_word:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Good guess!")

        # Check if the player has guessed the entire word
        if set(secret_word).issubset(set(guessed_letters)):
            print("\nCongratulations! You've guessed the word:", secret_word)
            print("You are The WINNER")
            break

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was:", secret_word)
        print("Do't STOP...Try again")

# Run the Hangman game
hangman()