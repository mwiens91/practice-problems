# @leet start
import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # k is in an integer that will be between 1 and the maximum pile
        # size. We can determine this k with a binary search on a
        # validation function.
        def is_valid(k: int) -> bool:
            time = 0

            for pile_size in piles:
                time += math.ceil(pile_size / k)

                # This lets us exit quicker for invalid piles, but does
                # require more checks of this condition. Not sure if
                # it's better to have this here or outside of the loop.
                # Doesn't really matter though.
                if time > h:
                    return False

            return True

        # Binary search
        max_pile = max(piles)

        i = 1
        j = max_pile

        while i < j:
            mid = (i + j) // 2

            if is_valid(mid):
                j = mid
            else:
                # Not valid
                i = mid + 1

        return i


# @leet end
