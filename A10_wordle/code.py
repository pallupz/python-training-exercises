# Exercise Name:
# 	A10_wordle
# Description:
# 	Create the wordle game
# Resources:
# 	Valid Words List: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93

from colorama import init, Back
from utils import get_random_word, get_valid_input
import copy


print('\n\n************* WELCOME TO WORDLE *************')

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
    print(f'{attempts - len(guesses)} attempts left. ')
    input_word = get_valid_input(valid_words)
    
    word_map_copy = copy.deepcopy(word_map)
    printls = []
    for idx, char in enumerate(input_word):
        if char in word_map_copy and word_map_copy[char]: # due to example: tubas tasty
            # print(word_map_copy)
            for pos in word_map_copy.get(char):
                if pos == idx:
                    printls.append(Back.GREEN + ' ' + char.upper() + ' ')
                    word_map_copy[char].remove(pos) # due to example: tubas tasty
                    break    
            else:
                word_map_copy[char].remove(pos) # due to example: hello hooly
                printls.append(Back.YELLOW + ' ' + char.upper() + ' ')
        else:
            printls.append(Back.WHITE + ' ' + char.upper() + ' ')
    
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
