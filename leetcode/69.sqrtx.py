# @leet start
class Solution:
    def mySqrt(self, x: int) -> int:
        # Idea: do a binary search to find largest y such that y^2 <= x
        start = 0
        end = x

        while start < end:
            mid = (start + end) // 2

            if mid**2 <= x:
                if (mid + 1) ** 2 <= x:
                    start = mid + 1
                else:
                    # Found the solution
                    return mid
            else:
                end = mid - 1
# @leet end
