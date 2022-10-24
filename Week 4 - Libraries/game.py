import random

# Prompt user for positive number and check validity
n = input('Level: ')

while not n.isnumeric() or int(n) <= 0:
    n = input('Level: ')

# Generate random number between 1 and n
rand_int = random.randint(1, int(n))

# Promt user to guess the random number and check validity
guess = input('Guess: ')

while not guess.isnumeric() or int(guess) <= 0:
    guess = input('Guess: ')

# Play the game
while True:

    if int(guess) < rand_int:
        print('Too small!')
        guess = input('Guess: ')
    elif int(guess) > rand_int:
        print('Too large!')
        guess = input('Guess: ')
    else:
        print('Just right!')
        break
