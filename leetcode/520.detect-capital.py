# @leet start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if word[0].isupper():
            # First char is uppercase. Assert all remaining chars are
            # either uppercase or lowercase
            if n == 1:
                return True

            if word[1].isupper():
                return all(word[i].isupper() for i in range(2, n))

            # word[1] is lowercase
            return all(word[i].islower() for i in range(2, n))

        # word[0] is lowercase
        return all(word[i].islower() for i in range(1, n))


# @leet end
