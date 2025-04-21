# @leet start
from collections import Counter


class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        # If k == len(nums), all numbers are candidates for the largest
        # almost missing number
        if k == len(nums):
            return max(nums)

        # Get the count of each number
        counts = Counter(nums)

        # If k == 1, the candidates are any value that appears exactly
        # once
        if k == 1:
            candidates = [num for num, count in counts.items() if count == 1]
        else:
            # 1 < k < len(nums): the only candidates are the first and
            # last elements provided that their values do not occur
            # elsewhere in the list
            candidates: list[int] = []

            if counts[nums[0]] == 1:
                candidates.append(nums[0])

            if counts[nums[-1]] == 1:
                candidates.append(nums[-1])

        # Return the maximum candidate if there are any candidates
        if candidates:
            return max(candidates)

        # No candidates
        return -1


# @leet end
