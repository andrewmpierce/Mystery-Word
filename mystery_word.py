import random
import re

master = open("/usr/share/dict/words")
dictionary = master.read()
dictionary = dictionary.lower().split()


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_word_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_word_list.append(word)
    return easy_word_list


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_word_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_word_list.append(word)
    return medium_word_list

def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_word_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list

def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    correct_word = random.choice(word_list)
    return correct_word

def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.
    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.
    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    progress_display = []
    for letter in word:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.append('_')
    progress_display = ' '.join(progress_display)
    progress_display = progress_display.upper()
    return progress_display


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    progress = display_word(word, guesses)
    if '_' in progress:
        return False
    else:
        return True

def main():
    """
    Runs when the program is called from the command-line.
    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    level = input("What difficulty setting do you want?\n")
    if level == 'easy':
        answer = random_word(easy_words(dictionary))
    elif level == 'medium':
        answer = random_word(medium_words(dictionary))
    else:
        answer = random_word(hard_words(dictionary))
    guesses = []
    fails = 0
    while is_word_complete(answer, guesses) == False:
        this_guess = (input("Okay, take a guess!\n")).lower()
        if this_guess not in guesses:
            if this_guess not in answer:
                fails += 1
        else:
            print("You must not be feeling well, you've already guessed that!")
        guesses.append(this_guess)
        print(display_word(answer, guesses))
        print("You have {} incorrect guesses left.".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        play_again_lose = input(("You lose! The word was {}. If you want to play again, enter yes.\n".format(answer)))
        if play_again_lose == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")
    else:
        play_again_win = input(("You won! If you want to play again, enter yes.\n"))
        if play_again_win == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")

if __name__ == '__main__':
    main()
