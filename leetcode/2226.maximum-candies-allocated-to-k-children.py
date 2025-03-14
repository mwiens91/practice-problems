# @leet start
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        # First sort the candy piles from largest to smallest
        candies.sort(reverse=True)

        # Define a function to determine if all children can receive a
        # target number of candies
        n = len(candies)

        def can_have_target_candies(target: int) -> bool:
            # Edge case: target == 0
            if target == 0:
                return True

            # Keep track of the number of children that have received
            # candies
            received_count = 0

            # Go through piles and give target number of candies to
            # children until all k children have target candies
            pile_idx = 0

            while received_count < k:
                # Return False if we've run out of piles or if the
                # current pile doesn't have target number of candies
                if pile_idx >= n or candies[pile_idx] < target:
                    return False

                received_count += candies[pile_idx] // target
                pile_idx += 1

            return True

        # Find the number of candies to give children using a binary
        # search
        low = 0
        high = candies[0]

        while low <= high:
            mid = (low + high) // 2

            if can_have_target_candies(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high


# @leet end
