import pathlib
import random
import sys
from string import ascii_letters
g_FILENAME = "wordlist.txt"
 
def main():
    # Pre-process
    word = get_random_word()

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess()
        if guess == word:
            break

    # Post-process
    else:
        game_over()


def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(word, guess) if correct == letter
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)
        
    print("correct Letters: ", "".join(sorted(correct_letters)))    
    print("misplaced Letters: ", "".join(sorted(misplaced_letters)))
    print("wrong Letters: ", "".join(sorted(wrong_letters)))
    

def game_over(word):
    print("The word was: ", word)
    print("Game Over!")

#returns the word to be guessed by the user
#Grabs the list of random words from the wordlist.txt file
def get_random_word():
    word_list = pathlib.Path(__file__).parent / g_FILENAME
    sorted_words = sorted( # Sort words alphabetically
        # Read all words from the file
        {
            word.lower()
            # Filter out words that contain non-ASCII letters
            for word in word_list.read_text(encoding="utf-8").split()
            if all (letter in ascii_letters for letter in word) and (len(word) == 5)
        },
        # Sort words by length
        key=lambda word: (len(word), word), 
    )
    # Write the sorted words to the output file
    # out_path.write_text("\n".join(words), encoding="utf-8")
    return random.choice(sorted_words)

if __name__ == "__main__":
    main()