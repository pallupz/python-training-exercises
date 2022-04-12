# https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93

import random
from colorama import init, Back
from utils import get_random_word, get_valid_input

init(autoreset=True)
word = get_random_word()

with open('A10_wordle/valid-wordle-words.txt', 'r') as f:
    valid_words = f.read().splitlines()

word_map = {}
for idx, char in enumerate(word):
    if char in word_map:
        word_map[char].append(idx)
    else:
        word_map[char] = [idx]

guesses = []
answered = False
attempts = 6
while len(guesses) < attempts:
    input_word = get_valid_input(valid_words, attempts, len(guesses))
    
    printls = []
    for idx, char in enumerate(input_word):
        if char in word_map:
            for pos in word_map.get(char):
                if pos == idx:
                    printls.append(Back.GREEN + ' ' + char + ' ')
                    break    
            else:
                printls.append(Back.YELLOW + ' ' + char + ' ')
        else:
            printls.append(Back.WHITE + ' ' + char + ' ')
    
    guesses.append(printls)
    for guess in guesses:
        print()
        print(*guess)
    print('-------------------------')

    if input_word == word.lower():
        print("Congrats! That's the correct word!")
        answered = True
        break

if not answered:
    print(f'The word was: {word.upper()}')
    print('Better luck next time!')
