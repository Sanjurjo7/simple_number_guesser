import random

print('-------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('-------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
chance = 0

name = input('Player, what is your name? ')

while guess != the_number:
    chance += 1
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {}, your guess of {} is too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} is too HIGH.'.format(name, guess))
    else:
        print('Great job {}, it only took you {} tries to guess the number {}.'.format(name, chance, the_number))




