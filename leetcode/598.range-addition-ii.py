# @leet start
class Solution:
    def maxCount(
        self, m: int, n: int, ops: list[list[int]]
    ) -> int:
        if not ops:
            return m * n

        # Find minimum a_i and b_i from ops. The area covered by these
        # will be the number of maximum integers.
        return min(a for a, _ in ops) * min(b for _, b in ops)


# @leet end
