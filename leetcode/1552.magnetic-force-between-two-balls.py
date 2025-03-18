# @leet start
class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        # Sort the positions
        position.sort()

        # Define a function to see if a minimum magnetic force target is
        # possible. If the target force has a valid configuration, the
        # greedy configuration is also valid, where you place balls in
        # the closest possible bins that satisfy the force target.
        num_baskets = len(position)

        def minimum_force_is_possible(target: int) -> bool:
            balls_left = m - 1
            last_basket_idx_used = 0

            for i in range(1, num_baskets):
                if position[i] - position[last_basket_idx_used] >= target:
                    # Target force met. Place the ball in the basket.
                    balls_left -= 1
                    last_basket_idx_used = i

                    # Return True if we've used all balls
                    if balls_left == 0:
                        return True

            return False

        # Do a binary search to find the maximum minimum magnetic force
        low = 1
        high = (position[-1] - position[0]) // ((m - 2) if m > 2 else 1)

        while low <= high:
            mid = (low + high) // 2

            if minimum_force_is_possible(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high


# @leet end
