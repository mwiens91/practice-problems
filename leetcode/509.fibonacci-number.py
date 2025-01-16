# @leet start
class Solution:
    def fib(self, n: int) -> int:
        # Store results
        memo_list = [0] * max(2, n + 1)
        memo_list[1] = 1

        for i in range(2, n + 1):
            memo_list[i] = memo_list[i - 1] + memo_list[i - 2]

        return memo_list[n]


# @leet end
