# @leet start
from statistics import fmean


class Solution:
    def trimMean(self, arr: list[int]) -> float:
        # Get the number of smallest and largest elements to trim
        num_to_trim = len(arr) // 20

        return fmean(sorted(arr)[num_to_trim:-num_to_trim])


# @leet end
