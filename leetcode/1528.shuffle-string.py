# @leet start
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        n = len(s)
        unshuffled_chars = [""] * n

        for i in range(n):
            unshuffled_chars[indices[i]] = s[i]

        return "".join(unshuffled_chars)


# @leet end
