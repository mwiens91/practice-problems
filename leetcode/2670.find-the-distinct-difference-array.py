# @leet start
from collections.abc import Iterable


class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        def get_prefix_distinct_counts(it: Iterable[int]) -> list[int]:
            result: list[int] = []
            seen: set[int] = set()

            for x in it:
                seen.add(x)
                result.append(len(seen))

            return result

        prefix_distinct_counts = get_prefix_distinct_counts(nums)
        suffix_distinct_counts = get_prefix_distinct_counts(reversed(nums))[::-1]

        # Subtract from prefix values at each index i the suffix value at
        # i + 1
        return [
            prefix_count - suffix_count
            for prefix_count, suffix_count in zip(
                prefix_distinct_counts, suffix_distinct_counts[1:] + [0]
            )
        ]


# @leet end
