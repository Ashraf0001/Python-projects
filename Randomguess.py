import random

def guess(x):
    random_number = random.randint(1, x)

    while True:

        guess = int(input(f'Guess a number between the value 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Please guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print(f'wow , congrats. You have guessed the number {random_number} correctly!!')
            break




guess(8)

