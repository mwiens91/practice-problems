# @leet start
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        # Return "none" if nums cannot form a triangle
        a, b, c = nums

        if a + b <= c or a + c <= b or b + c <= a:
            return "none"

        # Return what type of triangle it is
        num_unique_sides = len(set(nums))

        if num_unique_sides == 1:
            return "equilateral"

        if num_unique_sides == 2:
            return "isosceles"

        return "scalene"


# @leet end
