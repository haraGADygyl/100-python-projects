import random


def picks():
    options = ["rock", "paper", "scissors"]

    user_pick = input("Your pick: ")
    ai_pick = random.choice(options)

    print(f"Computer pick: {ai_pick}")

    return user_pick, ai_pick


def play():
    while True:
        user_pick, ai_pick = picks()

        if user_pick == ai_pick:
            print("Draw!")
        elif user_pick == "rock" and ai_pick == "paper" or \
                user_pick == "paper" and ai_pick == "rock" or \
                user_pick == "scissors" and ai_pick == "paper":
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == '__main__':
    play()
