# @leet start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Find pairs of characters where the strings differ
        difference_pairs = [
            (char1, char2) for char1, char2 in zip(s1, s2) if char1 != char2
        ]

        # Return True if there are either 0 difference pairs, or if
        # there are exactly two and they are the reverse of each other
        return (
            len(difference_pairs) == 0
            or len(difference_pairs) == 2
            and difference_pairs[0] == difference_pairs[-1][::-1]
        )


# @leet end
