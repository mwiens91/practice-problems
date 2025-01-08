# @leet start
class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        current_sum = nums[0] + nums[1]
        sums_seen = set([current_sum])

        n = len(nums)

        for i in range(2, n):
            current_sum += nums[i] - nums[i - 2]

            if current_sum in sums_seen:
                return True

            sums_seen.add(current_sum)

        return False


# @leet end
