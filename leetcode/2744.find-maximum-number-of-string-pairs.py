# @leet start
class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        words_set = set(words)

        # Count all pairs
        count = 0

        while words_set:
            word = words_set.pop()
            reversed_word = word[::-1]

            if reversed_word in words_set:
                count += 1
                words_set.remove(reversed_word)

        return count


# @leet end
