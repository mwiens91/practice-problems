# @leet start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Optimization: if m > n, just return the sum of numbers
        if m > n:
            return sum(range(1, n + 1))

        # Return sum of numbers not divisible by m minus sum of numbers
        # divisible by m
        return sum(range(1, n + 1)) - 2 * sum(x for x in range(1, n + 1) if x % m == 0)


# @leet end
