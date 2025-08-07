# @leet start
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)

        return sum(set(word).issubset(allowed_set) for word in words)


# @leet end
