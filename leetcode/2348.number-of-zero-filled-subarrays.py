# @leet start
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0

        start = 0

        while start < n:
            # Find start and end of next zero-filled subarray
            while start < n and nums[start] != 0:
                start += 1

            if start >= n:
                break

            end = start + 1  # end is exclusive

            while end < n and nums[end] == 0:
                end += 1

            # Add to count
            subarray_len = end - start
            count += subarray_len * (subarray_len + 1) // 2

            # Set up for next iteration
            start = end + 1

        return count


# @leet end
