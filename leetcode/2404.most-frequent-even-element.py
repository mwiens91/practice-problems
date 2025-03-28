# @leet start
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        # Get the number of even counts
        even_counts = Counter(num for num in nums if num % 2 == 0)

        # If there are no even numbers, return -1
        if not even_counts:
            return -1

        # Return the smallest number with the maximum count
        max_count = max(even_counts.values())

        return min(num for num, count in even_counts.items() if count == max_count)


# @leet end
