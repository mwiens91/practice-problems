# @leet start
from collections import defaultdict


class Solution:
    def largestValsFromLabels(
        self, values: list[int], labels: list[int], numWanted: int, useLimit: int
    ) -> int:
        # Sort both values and labels in order of descending value
        values, labels = zip(*sorted(zip(values, labels), reverse=True))

        # Keep count of how many of a given label we have, the number of
        # items we have, and the value sum
        label_counts: defaultdict[int, int] = defaultdict(int)
        item_count = 0
        value_sum = 0

        # Greedily get as many high value items as possible
        for value, label in zip(values, labels):
            if label_counts[label] < useLimit:
                label_counts[label] += 1
                item_count += 1
                value_sum += value

                # Get out if we've reached the maximum number of items
                if item_count >= numWanted:
                    break

        return value_sum


# @leet end
