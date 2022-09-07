import random

cards_type = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
cards_suite = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def random_card():
    return f'{random.choice(cards_suite)} of {random.choice(cards_type)}'


print(random_card())
