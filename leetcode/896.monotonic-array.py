# @leet start
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        # Go through consecutive pairs. If a pair is increasing, set a
        # flag to True; similarly, if a pair is decreasing, set a
        # different flag to True. Assert that both flags aren't True.
        increasing = False
        decreasing = False

        for num1, num2 in zip(nums, nums[1:]):
            if num1 < num2:
                increasing = True
            elif num1 > num2:
                decreasing = True

            if increasing and decreasing:
                return False

        return True


# @leet end
