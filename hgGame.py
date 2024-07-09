import random
from hangmanWords import word_list
from hangmanLogo import stages, logo

chosen_word = random.choice(word_list)
display = []
flag = True
length_of_word = len(chosen_word)
lives = 6
print(logo)

for letter in range(length_of_word):
    display += '_'
print(f'the solution is {chosen_word}.')
print(display)

while flag:
    guess = input("Guess a letter: ").lower()

    for position in range(length_of_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        elif letter in display[position]:
            print(f'You already guess {guess} ')
    if guess not in chosen_word:
        lives -= 1
        print(f'Letter {guess} not in word')
    print(display)

    if '_' not in display:
        flag = False
        print('You win')
    if lives == 0:
        flag = False
        print('You lost')

    print(stages[lives])