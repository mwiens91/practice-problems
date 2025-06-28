# @leet start
class Solution:
    def sortSentence(self, s: str) -> str:
        shuffled_words = s.split()
        unshuffled_words = [""] * len(shuffled_words)

        # Iterate through each word and index encoded in each shuffled
        # word and place them in unshuffled words
        for word, idx in map(lambda w: (w[:-1], int(w[-1]) - 1), shuffled_words):
            unshuffled_words[idx] = word

        return " ".join(unshuffled_words)


# @leet end
