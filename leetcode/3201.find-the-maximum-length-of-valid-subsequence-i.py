# @leet start
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # Take mod 2 of all elements: the longest valid subsequence will
        # either have all of the same bit or alternating bits
        ones_count = 0
        zeros_count = 0

        alternating_count = 1
        alternating_last_bit = nums[0] % 2

        for num in nums:
            bit = num % 2

            if bit == 0:
                zeros_count += 1
            else:
                ones_count += 1

            if alternating_last_bit != bit:
                alternating_count += 1
                alternating_last_bit = bit

        return max(ones_count, zeros_count, alternating_count)


# @leet end
