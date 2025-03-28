# @leet start
import itertools


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # Represent all possible subsequence sums. We can do this by
        # combining 0 with all prefix sums of sorted numbers in a list.
        prefix_sums = [0] + list(itertools.accumulate(sorted(nums)))

        # For each query, find the maximum length sequence that has sum
        # less than or equal to the query
        num_prefix_sums = len(prefix_sums)
        answers = []

        for query in queries:
            left = 0
            right = num_prefix_sums - 1

            while left <= right:
                mid = (left + right) // 2

                if prefix_sums[mid] <= query:
                    left = mid + 1
                else:
                    right = mid - 1

            answers.append(right)

        return answers


# @leet end
