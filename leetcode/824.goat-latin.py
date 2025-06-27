# @leet start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        VOWELS = {"a", "e", "i", "o", "u"}

        result_words: list[str] = []

        for i, word in enumerate(sentence.split(), start=1):
            if word[0].lower() not in VOWELS:
                word = word[1:] + word[0]

            result_words.append(word + "ma" + "a" * i)

        return " ".join(result_words)


# @leet end
