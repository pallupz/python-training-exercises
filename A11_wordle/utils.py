import random

def get_random_word():
    with open('A11_wordle/valid-wordle-words.txt', 'r') as f:
        words = f.readlines()

    word = random.choice(words)[:-1]
    return word

def get_valid_input(valid_words, attempts, guess_count):
    in_word = input(f'{attempts - guess_count} attempts left. Enter guess: ')
    if in_word.lower() in valid_words:
        return in_word.lower()
    else:
        print('That is not a valid word')
        return get_valid_input(valid_words)