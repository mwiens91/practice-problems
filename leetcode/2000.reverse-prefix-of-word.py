# @leet start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            first_ch_idx = word.index(ch)

            return word[: first_ch_idx + 1][::-1] + word[first_ch_idx + 1 :]
        except ValueError:
            return word


# @leet end
