questions = {'q1': '1', 'q2': '2', 'q3': '3'}


def game():
    score = 0

    for k in questions:
        print(k)

        answer = input('Enter your answer: ')

        if answer == questions[k]:
            score += 1
            print('Correct!')
        else:
            print(f'Incorrect! The answer was {questions[k]}')

    return f'\nYour score is {score}!'


print(game())
