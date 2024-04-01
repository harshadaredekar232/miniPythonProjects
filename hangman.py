import random


def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "watermelon"]
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word.")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        print(display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            return

    print("Sorry, you ran out of attempts. The word was:", word)


hangman()
