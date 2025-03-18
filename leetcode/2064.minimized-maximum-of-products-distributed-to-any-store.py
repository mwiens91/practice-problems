# @leet start
import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        # Define a function to determine if it is possible to distribute
        # a maximum target quantity of products to each store
        def possible_to_distribute_at_most_target(target: int) -> bool:
            # For each product type, distribute it in the minimum number
            # of chunks that are at most target
            distributed_count = 0

            for quantity in quantities:
                distributed_count += math.ceil(quantity / target)

                # If we have to distribute to more than n stores, it is
                # not possible
                if distributed_count > n:
                    return False

            return True

        # Do a binary search to find the minimum maximum quantity of
        # products any given store receives
        low = max(1, sum(quantities) // n)
        high = max(quantities)

        while low <= high:
            mid = (low + high) // 2

            if possible_to_distribute_at_most_target(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low


# @leet end
