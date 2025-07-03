# @leet start
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]

        while len(word) < k:
            word += [chr(ord(char) + 1) for char in word]

        return word[k - 1]


# @leet end
