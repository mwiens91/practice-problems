# @leet start
class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        n = len(nums)

        have_removed = False

        for i in range(1, n):
            # Encountered a pair that isn't strictly increasing
            if nums[i - 1] >= nums[i]:
                # Either we remove the previous element or this
                # element. If this isn't possible, or we have already
                # removed an element, return False.
                if have_removed or not (
                    (i == 1 or nums[i - 2] < nums[i])
                    or (i == n - 1 or nums[i - 1] < nums[i + 1])
                ):
                    return False

                have_removed = True

        return True


# @leet end
