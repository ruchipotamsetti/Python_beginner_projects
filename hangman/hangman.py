import random
from words import words
import string

def get_valid_words():
    word = random.choice(words) #randomly chooses a word from a list 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_words()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters that user has guessed
    lives = 6
    

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        print(f"You have {lives} lives left and you used these letters:", ' '.join(used_letters))

        # what current word is (i.e W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Currents word: ",' '.join(word_list))

        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print('Letter is not in the word.')

        elif user_letter in used_letters: 
                print("You have already used that character. Please try again.")

        else:
                print("Invalid character. Please try again.")

    # gets here when len(word_letters) == 0 OR when lives == 0

    if lives == 0:
        print("\nYou died, sorry. The word was", word.upper())
    else: 
        print(f"\nYay you guessed the word, {word.upper()} !!")

hangman()
