# @leet start
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]
        reversed_substrings = set(
            reversed_s[i : i + 2] for i in range(len(reversed_s) - 1)
        )

        for i in range(len(s) - 1):
            if s[i : i + 2] in reversed_substrings:
                return True

        return False


# @leet end
