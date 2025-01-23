# @leet start
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        # We'll start from the back and move to the front, keeping track
        # of the longest arithmetic sequence we have found so far that
        # uses the current element
        longest_sequence_seen_dict = defaultdict(int)

        for num in reversed(arr):
            longest_sequence_seen_dict[num] = (
                1 + longest_sequence_seen_dict[num + difference]
            )

        return max(longest_sequence_seen_dict.values())


# @leet end
