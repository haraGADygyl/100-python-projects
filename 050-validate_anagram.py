def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


print(is_anagram('cinema', 'iceman'))
print(is_anagram('cinema', 'iceman1'))
