# @leet start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # All answers the same mod 2 (n - 1)
        time %= 2 * (n - 1)

        # Passing right
        if time // n == 0:
            return 1 + time

        # Passing left. It takes n - 1 seconds to reach the final person
        # passing right, then it gets passed to the left to the
        # (n - (time - (n - 1))th person.
        return 2 * n - time - 1


# @leet end
