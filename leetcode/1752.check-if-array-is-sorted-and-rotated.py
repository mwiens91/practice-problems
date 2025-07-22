# @leet start
class Solution:
    def check(self, nums: list[int]) -> bool:
        # There can be at most one pivot where the array is decreasing
        found_pivot = False

        for prev, current in zip(nums, nums[1:] + nums[:1]):
            if prev > current:
                if found_pivot:
                    return False

                found_pivot = True

        return True


# @leet end
