# @leet start
class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)

        if n <= 3:
            return False

        # We need to find p and q such that
        # - nums[0:p + 1] is strictly increasing
        # - nums[p:q + 1] is strictly decreasing
        # - nums[q:n] is strictly increasing
        for i in range(1, n - 1):
            if nums[i - 1] == nums[i]:
                return False

            if nums[i - 1] > nums[i]:
                p = i - 1

                if p == 0:
                    return False

                break
        else:
            return False

        for i in range(p + 1, n):
            if nums[i - 1] == nums[i]:
                return False

            if nums[i - 1] < nums[i]:
                q = i - 1

                if q == p:
                    return False

                break
        else:
            return False

        for i in range(q + 1, n):
            if nums[i - 1] >= nums[i]:
                return False

        return True


# @leet end
