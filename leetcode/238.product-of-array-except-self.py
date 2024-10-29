# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Get length of nums
        nums_len = len(nums)

        # We're going to calculate the prefix product first and store it
        # in our solution array. We'll calculate the suffix product
        # later and multiply those terms straight into the solution
        # array, rather than creating separate arrays for the products
        # and multiplying them later
        solution = [0] * nums_len

        # Prefix
        last_prefix_prod = 1

        for i in range(0, nums_len):
            solution[i] = last_prefix_prod

            # Set up for next iteration
            last_prefix_prod *= nums[i]

        # Suffix
        last_suffix_prod = 1
        for i in range(nums_len - 1, -1, -1):
            solution[i] *= last_suffix_prod

            # Set up for next iteration
            last_suffix_prod *= nums[i]

        return solution
# @leet end
