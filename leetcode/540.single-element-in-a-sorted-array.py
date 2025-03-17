# @leet start
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # Edge case: only one element
        n = len(nums)

        if n == 1:
            return nums[0]

        # Now we do a binary search on all odd indices smallest odd
        # index i that satisfies nums[i] != nums[i - 1]. Using this i,
        # nums[i - 1] is the sole single element.
        odd_idxs = list(range(1, n, 2))

        # NOTE: in the binary search, left, right, and mid refer to
        # indices of the odd_idxs list
        num_odd_idxs = len(odd_idxs)

        left = 0
        right = num_odd_idxs - 1

        while left <= right:
            mid = (left + right) // 2

            odd_idx = odd_idxs[mid]

            if nums[odd_idx] != nums[odd_idx - 1]:
                # We've already passed the sole single element
                right = mid - 1
            else:
                # We haven't passed the sole single element
                left = mid + 1

        # Return the answer
        if left == num_odd_idxs:
            # There was no odd index satisfying the condition, so the
            # last element is the sole single element
            return nums[-1]

        smallest_odd_idx_after_single_element = odd_idxs[left]

        return nums[smallest_odd_idx_after_single_element - 1]


# @leet end
