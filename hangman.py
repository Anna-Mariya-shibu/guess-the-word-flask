import random
import os

# Clear screen function for neat output
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Word bank
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

# Hangman stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Setup
guessedWord = ['_'] * len(word)
attempts = len(hangman_stages) - 1  # 6 wrong guesses allowed

print("Welcome to Hangman! 🎮")

# Game loop
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    clear_screen()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("✅ Great guess!")
    else:
        attempts -= 1
        print(hangman_stages[len(hangman_stages) - 1 - attempts])
        print("❌ Wrong guess! Attempts left:", attempts)

    if '_' not in guessedWord:
        print("\n🎉 Congratulations!! You guessed the word:", word)
        break

if attempts == 0 and '_' in guessedWord:
    print("\n💀 Game Over! The word was:", word)
    print(hangman_stages[-1])
