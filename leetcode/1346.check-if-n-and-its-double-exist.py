# @leet start
from collections import Counter


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        # Get counts of nums
        counts = Counter(arr)

        # See if any numbers double is in the counter. For the special
        # case of zero, we need to make sure there at least two of them.
        for num in counts:
            if num != 0:
                if 2 * num in counts:
                    return True
            else:
                if counts[0] >= 2:
                    return True

        return False


# @leet end
