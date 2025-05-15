# @leet start
class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(groups)

        last_digit = groups[0]
        result = [words[0]]

        for i in range(1, n):
            if groups[i] != last_digit:
                result.append(words[i])
                last_digit = groups[i]

        return result


# @leet end
