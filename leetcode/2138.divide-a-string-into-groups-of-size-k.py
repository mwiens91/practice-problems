# @leet start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result: list[str] = []

        # Get groups of size k not needing fill characters
        n = len(s)
        num_full_groups = n // k

        for i in range(num_full_groups):
            result.append(s[i * k : (i + 1) * k])

        # Get the (possible) final group needing fill characters
        if num_remaining_chars := n % k:
            result.append(s[num_full_groups * k :] + fill * (k - num_remaining_chars))

        return result


# @leet end
