# @leet start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # Define lower and upper threshold at and beyond which we won't
        # consider numbers
        n = len(nums)

        lower_threshold = 0
        upper_threshold = n + 1

        # We'll do a circular sort here for numbers 1 to n, ignoring all
        # other numbers. We do at most n swaps because each swap puts a
        # number in its correct place, from where it will not move
        # again. The count for the smallest integer starting at 1 rather
        # than 0 makes us do 1-indexing essentially, which is annoying.
        for i in range(n):
            num = nums[i]

            while (
                num != i + 1
                and lower_threshold < num < upper_threshold
                and nums[num - 1] != num   # This is for handling duplicates
            ):
                # Put num where it belongs, and put the thing where it
                # moved into i
                tmp = nums[num - 1]
                nums[num - 1] = num
                nums[i] = tmp

                # Continue until num == i + 1 or num is invalid
                num = tmp

        # Go through again and return the first index where num != i + 1
        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1

        # All indices had num == i + 1
        return n + 1
# @leet end
