# @leet start
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        # Given an existing nice subarray, let s be the bitwise OR of
        # all its elements. We can add a new element x to the nice
        # subarray only if s & x == 0. We'll use a sliding window,
        # continually adding elements from the right while the condition
        # is satisfied. If the above condition is not satisfied, we
        # remove elements from the left y with s ^ y (this removes all 1
        # bits in s that came from y) until the condition is satisfied
        # for the next element x. Then we repeat, keeping track of the
        # longest nice subarray as we go.
        n = len(nums)

        longest_nice_subarray = 1
        bitwise_or_of_subarray = nums[0]

        # The left index is the beginning of the nice subarray. The
        # right index is one past the end of the nice subarray.
        left = 0
        right = 1

        while right < n:
            # Add elements from the right to the nice subarray
            while right < n and bitwise_or_of_subarray & nums[right] == 0:
                bitwise_or_of_subarray |= nums[right]

                right += 1

            # Update longest nice subarray
            longest_nice_subarray = max(longest_nice_subarray, right - left)

            # Remove elements from the left until we are able to add the
            # next element from the right
            while right < n and bitwise_or_of_subarray & nums[right] != 0:
                bitwise_or_of_subarray ^= nums[left]

                left += 1

        return longest_nice_subarray


# @leet end
