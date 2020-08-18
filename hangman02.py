# Hangman game
import random

word_list = ['python', 'java', 'kotlin', 'javascript']

def chosen_word():
    return random.choice(word_list)
# ----------------------------------------------
secret_word = chosen_word()
print('HANGMAN')

def game():
    
    hint = list('-'*len(secret_word))
    letters_guessed = []
    mistake_made = 0

    while mistake_made < 8:
        guess = str(input(f"\n{''.join(hint)}\nInput a letter: "))
        if guess in secret_word and guess not in letters_guessed:
            letters_guessed.append(guess)
            index_of_guess = [index for index, element in enumerate(list(secret_word)) if element == guess]  # this line get the index of guesses
            for index in index_of_guess: 
                hint[index] = guess  # replace the '-' in hint with guess at designed index
            # check if the result is true
            if hint == list(secret_word):
                print(f'\n{secret_word}')
                print('You guessed the word! \nYou survived!')
                break
            else:
                continue
        
        elif guess in letters_guessed:
            mistake_made += 1
            print('No improvements')
            
        elif guess not in secret_word and guess not in letters_guessed:
            letters_guessed.append(guess)
            mistake_made += 1
            print('No such letter in the word')
            
        # stop the game after 8 mistakes
        if mistake_made == 8:
            print('You are hanged!')
            break
        else:
            continue
         
            
game()
        
    
    
