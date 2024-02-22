import random

import hangman_art
import hangman_words

word_list = hangman_words.word_list
display = []

selected_word = hangman_words.word_list[random.randint(0, len(word_list) - 1)]
player_lives = 6
win = False

for i in range(len(selected_word)):
    display.append("_")

print(hangman_art.logo)

while player_lives != 0:
    print(hangman_art.stages[player_lives])
    print(f"Complete the word: {''.join(display)}")
    user_guess = input("Guess a letter: ").lower()

    if user_guess in display:
        print(f'\n\n\n\nYou already guessed "{user_guess}"')


    turn_ok = False

    for i in range(len(selected_word)):
        char = selected_word[i]
        if char == user_guess:
            display[i] = char
            turn_ok = True

    if not turn_ok:
        print(f'\n\n\n\nYou guessed a letter that is not in the word. You lose a life.')
        player_lives -= 1

if "_" not in display:
    win = "True"

if win:
    print("You win!")
else:
    print(hangman_art.stages[player_lives])
    print(f"You Lose. The word was: {selected_word}")
