from collections import Counter, defaultdict


def count_characters(s):
    counter = Counter(s)

    return counter


text = 'Thecleverprogrammer'
print(count_characters(text))


def count_characters2(s):
    result = defaultdict(int)
    for c in s:
        result[c] += 1

    return result


print(count_characters2(text))
