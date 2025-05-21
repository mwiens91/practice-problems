# @leet start
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # Sort nums from largest to smallest
        nums.sort(reverse=True)

        # Find the highest perimeter triangle, if one exists. Iterate
        # through largest possible larger sides. Since for a triangle we
        # require the sum of the other two sides to be larger than the
        # largest side, we only need to test if for a given largest
        # side, whether the largest possible other sides less than or
        # equal to the largest side can form a triangle.
        for i in range(n - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return sum(nums[i : i + 3])

        return 0


# @leet end
