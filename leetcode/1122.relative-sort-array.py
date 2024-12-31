# @leet start
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # Store result in a list
        res = []

        # Put numbers in arr2 at the beginning of the result
        arr1_counts = Counter(arr1)

        for num in arr2:
            res += [num] * arr1_counts[num]

        # Put the numbers not in arr2 at the end of the result in sorted
        # order
        arr1_unique_vals = set(arr1_counts) - set(arr2)

        for num in sorted(arr1_unique_vals):
            res += [num] * arr1_counts[num]

        return res


# @leet end
