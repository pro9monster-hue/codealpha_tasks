import random

WORD_LIST = ["python", "intern", "code", "alpha", "challenge"]
MAX_INCORRECT_GUESSES = 6

def play_hangman():
    word = random.choice(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\n" + display_word)
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(list(guessed_letters)))}")

        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word}")
            return

        while True:
            try:
                guess = input("Guess a letter: ").lower()
                if len(guess) != 1 or not 'a' <= guess <= 'z':
                    print("Please enter a single, valid letter.")
                elif guess in guessed_letters:
                    print("You already guessed that letter. Try again.")
                else:
                    break
            except EOFError:
                return

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    print("\nGame Over!")
    print(f"The word was: {word}")

if __name__ == "__main__":
    play_hangman()
