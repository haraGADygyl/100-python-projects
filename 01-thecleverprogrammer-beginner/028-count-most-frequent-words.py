from collections import Counter

with open("resources/words.txt", encoding="UTF-8") as f:
    words = Counter(f.read().split()).most_common(5)

    for word in words:
        print(f"{word[0]}: {word[1]}")
