# @leet start
class Solution:
    def distinctIntegers(self, n: int) -> int:
        # We can perform 10^9 operations, and n <= 100. If n == 1, then
        # only 1 will be on the board. Assume n > 1. It is guaranteed
        # that on the ith operation, i < n - 1, n - i will be on the
        # board. This is because on the first day, n - 1 is added since
        # n % n - 1 == 1; on the second day, n - 2 is either already
        # present or is added since n - 1 % n - 2 == 1; and so on.
        return 1 if n == 1 else n - 1


# @leet end
