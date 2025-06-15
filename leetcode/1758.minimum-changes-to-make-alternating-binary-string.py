# @leet start
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        possible_transformations = [
            "".join(str(i % 2) for i in range(n)),
            "".join(str(i % 2) for i in range(1, n + 1)),
        ]

        return min(
            sum(b1 != b2 for b1, b2 in zip(s, transformation))
            for transformation in possible_transformations
        )


# @leet end
