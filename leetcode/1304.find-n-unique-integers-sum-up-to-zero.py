# @leet start
class Solution:
    def sumZero(self, n: int) -> list[int]:
        res = []

        # If n odd, add 0 to the list
        if n % 2 == 1:
            res.append(0)
            n -= 1

        # Add remaining nums
        for x in range(1, n // 2 + 1):
            res += [x, -x]

        return res


# @leet end
