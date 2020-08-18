# Hangman game
import random

print('HANGMAN')


def game():
    while True:
        word_list = ['python', 'java', 'kotlin', 'javascript']
        secret_word = random.choice(word_list)
        hint = list('-' * len(secret_word))
        letters_guessed = []
        mistake_made = 0

        trigger = str(input('Type "play" to play the game, "exit" to quit: '))
        if trigger == "play":
            while mistake_made < 8:
                guess = str(input(f"\n{''.join(hint)}\nInput a letter: "))
                if guess.isascii() and guess.islower() and len(guess) == 1:
                    if guess in secret_word and guess not in letters_guessed:
                        letters_guessed.append(guess)
                        # the following line of code get the index of guesses
                        index_of_guess = [index for index, element in enumerate(list(secret_word)) if element == guess]
                        for index in index_of_guess:
                            hint[index] = guess  # replace the '-' in hint with guess at designed index
                        # check if the result is true
                        if hint == list(secret_word):
                            print(f'\n{secret_word}')
                            print('You guessed the word! \nYou survived!\n')
                            break
                        else:
                            continue

                    elif guess in letters_guessed:
                        print('You already typed this letter')

                    elif guess not in secret_word:
                        letters_guessed.append(guess)
                        mistake_made += 1
                        print('No such letter in the word')

                    # stop the game after 8 mistakes
                    if mistake_made == 8:
                        print('You are hanged!\n')
                    else:
                        continue

                elif len(guess) != 1:
                    print('You should input a single letter')
                    continue

                else:
                    print('It is not an ASCII lowercase letter')
                    continue

        elif trigger == "exit":
            exit()


game()
