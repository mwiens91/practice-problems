# @leet start
import functools


class Solution:
    def isHappy(self, n: int) -> bool:
        # This question boils down to detecting if we're in a loop or
        # not. From my understanding there's no other way to know ahead
        # whether a number is happy or not.
        seen = set()

        while n != 1:
            # Check if loop detected
            if n in seen:
                return False

            # Add this n to the seen set
            seen.add(n)

            # Transform n to the sum of its squares
            n = functools.reduce(lambda x, y: x + y, [int(x) ** 2 for x in str(n)])

        # n became 1
        return True


# @leet end
