import pathlib
import random
import sys
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme
console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

g_FILENAME = "wordlist.txt"
 
def main():
    # Pre-process
    word = get_random_word().upper()
    console.print(f"word: {word}")
    guesses = ["_" * 5] * 6
    
    # Process (main loop)
    for guess_num in range(6):
        refresh_page(headline=f"Guess {guess_num+1}")
        show_guesses(guesses, word)
        
        guesses[guess_num] = input(f"\nGuess word: ").upper()
        if guesses[guess_num] == word:
            print("You win!")
            break

    # Post-process
    else:
        game_over(word)


def show_guesses(guesses, word):
    for guess in guesses:
        styled_guesses = []
        for letter, correct in zip(guess,word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guesses.append(f"[{style}]{letter}[/]")
        console.print(" ".join(styled_guesses), justify="center")
    
    
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


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()