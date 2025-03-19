# @leet start
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # We can be greedy here. We iterate through the array and flip
        # the current and following two indices each time we encounter a
        # 0.
        n = len(nums)

        count = 0

        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the next two indices. We don't need to flip the
                # current bit; we only need to count that we've flipped
                # it.
                for j in range(1, 3):
                    nums[i + j] = (nums[i + j] + 1) % 2

                count += 1

        return count


# @leet end
