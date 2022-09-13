from difflib import SequenceMatcher


def sequence_matcher(seq1, seq2):
    sequence_score = SequenceMatcher(None, seq1, seq2).ratio()
    return sequence_score


text1 = "My name is John"
text2 = "Hello, my name is John"
text3 = "Some other text here"

print(f"Texts are {sequence_matcher(text1, text2) * 100:.2f}% similar")
print(f"Texts are {sequence_matcher(text1, text3) * 100:.2f}% similar")
