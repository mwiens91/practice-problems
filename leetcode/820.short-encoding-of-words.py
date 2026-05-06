# @leet start
class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        keep = set(words)

        for word in words:
            for i in range(1, len(word)):
                keep.discard(word[i:])

        return sum(len(s) + 1 for s in keep)


# @leet end
