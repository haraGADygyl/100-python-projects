name = input('Enter your name: ')

print(f'{name}, you saw a princes, guarded by a huge dragon. What do you do? ')
print('Press 1 for run away, press 2 to fight the dragon')

pick = int(input('1 or 2?\n'))

if pick == 1:
    print('Indeed a wise choice!')
else:
    print('You fool!')
