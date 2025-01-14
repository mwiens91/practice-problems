# @leet start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Find if something is a perfect square with a binary search
        left = 0
        right = num

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid**2

            if mid_squared == num:
                return True

            if mid_squared < num:
                left = mid + 1
            else:
                # mid_squared > num
                right = mid - 1

        return False


# @leet end
