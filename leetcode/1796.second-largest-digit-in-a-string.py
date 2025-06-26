# @leet start
class Solution:
    def secondHighest(self, s: str) -> int:
        digits_sorted = sorted(
            set(map(int, (char for char in s if char.isdigit()))), reverse=True
        )

        if len(digits_sorted) >= 2:
            return digits_sorted[1]

        return -1


# @leet end
