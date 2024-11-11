# @leet start
from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        # Count the occurances of each string
        arr_counter = Counter(arr)

        # Now find the kth distinct string
        distinct_count = 0  # increment this each time we hit a distinct string

        for str_ in arr:
            if arr_counter[str_] == 1:
                distinct_count += 1

            if distinct_count == k:
                return str_

        # If we get here that means the number of distinct strings is
        # less than k, so we need to return an empty string
        return ""


# @leet end
