with open("../resources/capital_letters.txt", encoding="UTF-8") as f:
    counter = 0
    for a in f.read():
        if a.isupper():
            counter += 1

    print(counter)
