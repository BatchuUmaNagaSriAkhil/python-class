#Problem 3 — Sentence Analyzer System
class EmptySentenceError(Exception):
    pass


class InvalidSentenceError(Exception):
    pass


class SentenceTooLongError(Exception):
    pass


class SentenceAnalyzer:

    def analyze(self, sentence):

        if sentence == "":
            raise EmptySentenceError(
                "EmptySentenceError: Sentence cannot be empty."
            )

        if sentence.isdigit():
            raise InvalidSentenceError(
                "InvalidSentenceError: Sentence cannot contain only digits."
            )

        if len(sentence) > 100:
            raise SentenceTooLongError(
                "SentenceTooLongError: Sentence exceeds maximum length."
            )

        vowels = 0

        for i in sentence.lower():
            if i in "aeiou":
                vowels += 1

        words = len(sentence.split())

        uppercase = 0

        for i in sentence:
            if i.isupper():
                uppercase += 1

        print("Vowels:", vowels)
        print("Words:", words)
        print("Uppercase Letters:", uppercase)


sentence = input()

obj = SentenceAnalyzer()

try:
    obj.analyze(sentence)

except Exception as e:
    print(e)
    