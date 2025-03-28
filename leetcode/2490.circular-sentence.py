# @leet start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        num_words = len(words)

        for i in range(num_words):
            if words[i][-1] != words[(i + 1) % num_words][0]:
                return False

        return True


# @leet end
