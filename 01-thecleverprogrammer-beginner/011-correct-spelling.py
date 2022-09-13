from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter a word: ")

if word in corrector:
    print("Correct!")
else:
    correct_word = corrector.correction(word)
    print(f"Correct word is: {correct_word}")
