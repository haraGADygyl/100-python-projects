question_words = ["what", "why", "when", "where",
                  "name", "is", "how", "do", "does",
                  "which", "are", "could", "would",
                  "should", "has", "have", "whom", "whose", "don't"]

question = input("Write something:\n ")


def is_question(q_words):
    for word in q_words:
        if question.startswith(word.lower()):
            return "This is a question!"
    return "This is not a question!"


print(is_question(question_words))
