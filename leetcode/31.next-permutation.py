# @leet start
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Handle edge case of n = 1
        n = len(nums)

        if n == 1:
            return

        # Idea: from back of the array to front, go pairwise until we
        # encounter the first pair (x, y) (index of x is one less than
        # y) such that x < y. This is one of two elements we will swap,
        # call it the "pivot" p. The element we swap with is the
        # rightmost digit q such that q > p. Example:
        #
        # 6 4 7 5 3 2 1,
        #
        # p = 4,
        # q = 5.
        #
        # After the swap we have
        #
        # 6 5 7 4 3 2 1.
        #
        # Note that all digits after the pivot are in non-increasing
        # order. To get the next permutation we just need to reverse the
        # digits after the pivot

        # Find pivot
        right_idx = n - 1
        left_idx = n - 2

        # We'll get left number in the loop itself
        right = nums[right_idx]

        pivot = None
        pivot_idx = None

        while left_idx >= 0:
            left = nums[left_idx]

            # Found pivot
            if left < right:
                pivot = left
                pivot_idx = left_idx
                break

            # Continue
            right = left

            right_idx -= 1
            left_idx -= 1

        # Now find the other digit to swap and do the swap
        if pivot is not None:
            right_idx = n - 1

            swap_idx = None

            while True:
                right = nums[right_idx]

                # Found pivot
                if pivot < right:
                    swap_idx = right_idx
                    break

                right_idx -= 1

            nums[pivot_idx], nums[swap_idx] = nums[swap_idx], nums[pivot_idx]

        # Reverse digits after the pivot
        if pivot is None:
            pivot_idx = -1

        left_idx = pivot_idx + 1
        right_idx = n - 1

        while left_idx < right_idx:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

            left_idx += 1
            right_idx -= 1

        return


# @leet end
