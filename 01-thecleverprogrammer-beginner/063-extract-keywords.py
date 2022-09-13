from rake_nltk import Rake

r = Rake()

with open('resources/words_intro.txt') as text:
    r.extract_keywords_from_text(text.read())

    print(r.get_ranked_phrases_with_scores())
