import random

random_number = random.randint(1, 10)

while True:
    user_number = int(input("Pick a number between 1 and 10: "))

    if user_number < random_number:
        print("It's bigger than that")
        continue
    elif user_number > random_number:
        print("It's smaller than that")
        continue
    else:
        print("You have guessed it!")
        break
