
word = "TESTVALUE"

for user_guess in range(1,7):
    guess = input("Guess a letter: ").upper()
    
    #If the guess is correct, end the game
    if guess == word:
        print("Correct!")
    
    correct_letters = {
        letter for letter, correct in zip(word, guess) if correct == letter
    }
    

    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)
    
    print(f"Correct letters: {correct_letters}")
    print(f"Misplaced letters: {misplaced_letters}")
    print(f"Wrong letters: {wrong_letters}")