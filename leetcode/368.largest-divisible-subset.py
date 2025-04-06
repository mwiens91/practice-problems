# @leet start
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        # We'll go through each num in sorted order and for each num
        # find the maximum subset size with num as its largest element
        # using previous results
        nums.sort()
        n = len(nums)

        max_subset_sizes = [1] * n
        prev_result_idx_used: dict[int, int] = {}

        for i in range(1, n):
            # Find the max subset size of an element nums_j, j < i, such
            # that nums_j divides nums_i: we use this subset as a base.
            #
            # It's a small detail, but it's slightly more efficient to
            # go through reverse order with this next loop
            for j in range(i - 1, -1, -1):
                if (
                    nums[i] % nums[j] == 0
                    and max_subset_sizes[j] + 1 > max_subset_sizes[i]
                ):
                    max_subset_sizes[i] = max_subset_sizes[j] + 1
                    prev_result_idx_used[i] = j

        # Build the maximum subset
        max_subset = []
        next_idx: int | None = max_subset_sizes.index(max(max_subset_sizes))

        while next_idx is not None:
            max_subset.append(nums[next_idx])
            next_idx = prev_result_idx_used.get(next_idx, None)

        return max_subset


# @leet end
