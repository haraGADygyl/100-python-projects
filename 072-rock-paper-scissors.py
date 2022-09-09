import random

player_choice = input('Pick rock, paper or scissors: ')

options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)
print(computer_choice)

if player_choice == computer_choice:
    print('Draw!')
elif player_choice == 'rock' and computer_choice == 'paper' \
        or player_choice == 'rock' and computer_choice == 'scissors' \
        or player_choice == 'paper' and computer_choice == 'rock' \
        or player_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:
    print('You lose!')
