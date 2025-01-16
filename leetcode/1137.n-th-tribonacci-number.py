# @leet start
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0] * max(3, n + 1)
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n + 1):
            memo[i] = sum(memo[i - delta] for delta in range(1, 4))

        return memo[n]


# @leet end
