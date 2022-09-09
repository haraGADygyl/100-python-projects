import random

dice_count = int(input('How many dices will you roll?\n'))

while True:

    roll = dice_count * random.randint(1, 6)
    print(f'You rolled {roll}')

    play_again = input('Roll again? yes or no\n')

    if play_again == 'no':
        break
