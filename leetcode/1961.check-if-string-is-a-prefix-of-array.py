# @leet start
class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        # Go through each word, match it with the corresponding
        # characters in s, and ensure they match
        s_idx = 0

        for word in words:
            if s[s_idx : s_idx + len(word)] != word:
                return False

            s_idx += len(word)

            if s_idx == len(s):
                return True

        return False


# @leet end
