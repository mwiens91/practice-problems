# @leet start
from collections import Counter


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        counts = Counter(num[:3])

        # Since comparison operations will work find on strings, we'll
        # keep the maximum as a string—no need to convert to integer
        max_good_int = num[:3] if len(counts) == 1 else ""

        # Use a sliding window
        for i in range(3, len(num)):
            # Add new number
            counts[num[i]] += 1

            # Remove old number
            counts[num[i - 3]] -= 1

            if counts[num[i - 3]] == 0:
                del counts[num[i - 3]]

            # Update maximum good integer
            if len(counts) == 1:
                max_good_int = max(max_good_int, num[i - 2 : i + 1])

        return max_good_int


# @leet end
