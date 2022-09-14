numbers = [3, 4, 1, 2, 9]


def pair10(arr):
    numbers_seen = {}

    for item in arr:
        if 10 - item in numbers_seen:
            print(f'{10 - item}, {item}')
            return
        else:
            numbers_seen[item] = 1

    print("There is no pair that adds up to 10.")


def pair102(arr):
    for k in arr:
        if 10 - k in arr:
            print(f'{k}, {10 - k}')
            return
    else:
        print("There is no pair that adds up to 10.")


pair10([3, 4, 1, 2, 9])
pair10([-11, -20, 2, 4, 30])
pair10([1, 2, 9, 8])
pair10([1, 1, 1, 2, 3, 9])
pair10([1, 1, 1, 2, 3, 4, 5])
