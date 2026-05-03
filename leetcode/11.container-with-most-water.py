# @leet start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        best = 0
        left = 0
        right = len(height) - 1

        while left < right:
            best = max(best, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best


# @leet end
