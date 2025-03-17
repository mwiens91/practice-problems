# @leet start
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD_VALUE = 10**9 + 7

        # First, sort the nums
        nums.sort()

        # Keep track of the number of valid non-empty subsequences
        count = 0

        # For each smaller number x, find the largest number y such that
        # x + y <= target. We'll do binary searches in the loop below
        # where we can reuse results.
        n = len(nums)

        next_binary_search_right_idx = n - 1

        for i, smaller_number in enumerate(nums):
            # We want to find the largest number that is less than or
            # equal to the effective target
            effective_target = target - smaller_number

            # If the smaller number is larger than the effective target,
            # then there are no more valid non-empty subsequences to be
            # found
            if smaller_number > effective_target:
                break

            # Use a binary search to find the larger number. The index
            # of right will point to the largest number after the search
            # is complete.
            left = i
            right = next_binary_search_right_idx

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= effective_target:
                    left = mid + 1
                else:
                    right = mid - 1

            # Use the larger number index as the endpoint for the next
            # binary search
            next_binary_search_right_idx = right

            # Add to the count
            count = (count + 2 ** (right - i)) % MOD_VALUE

        return count


# @leet end
