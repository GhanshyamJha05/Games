import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

def main():
    print("Welcome to the Word Guessing Game!")
    
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts_remaining = 6

    while attempts_remaining > 0:
        print("\nWord to guess:", display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {attempts_remaining}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_remaining -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("\nOut of attempts! The word was:", word_to_guess)

if __name__ == "__main__":
    main()
