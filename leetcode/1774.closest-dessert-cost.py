# @leet start
import math


class Solution:
    def closestCost(
        self, baseCosts: list[int], toppingCosts: list[int], target: int
    ) -> int:
        # We can have 0 to 2 of each type of topping per base. Call any
        # combination of toppings an "extra". Find all possible extra
        # costs and sort them.
        possible_extra_costs = {0}

        for topping_cost in toppingCosts:
            new_extra_costs = set()

            for existing_extra_cost in possible_extra_costs:
                new_extra_costs.add(existing_extra_cost + topping_cost)
                new_extra_costs.add(existing_extra_cost + topping_cost * 2)

            possible_extra_costs.update(new_extra_costs)

        extra_costs = sorted(possible_extra_costs)

        # For each base cost, do a binary search to find the extra cost
        # closest to target - base cost (call this the "extra target")
        smallest_diff = math.inf
        best_cost = math.inf

        num_extra_costs = len(extra_costs)

        for base_cost in baseCosts:
            extra_target = target - base_cost

            # First find the leftmost insertion point where extra target
            # would go in the extra costs list
            left = 0
            right = num_extra_costs - 1

            while left <= right:
                mid = (left + right) // 2
                mid_cost = extra_costs[mid]

                if mid_cost < extra_target:
                    left = mid + 1
                else:
                    right = mid - 1

            # left is the insertion point after the above loop. Now
            # choose the extra cost closest to the extra target.
            if left == 0:
                closest_extra_cost = extra_costs[0]
            elif left == num_extra_costs:
                closest_extra_cost = extra_costs[-1]
            else:
                # If there are two equally close costs, choose the
                # smaller one
                smaller_extra_cost = extra_costs[left - 1]
                larger_extra_cost = extra_costs[left]

                closest_extra_cost = (
                    smaller_extra_cost
                    if abs(smaller_extra_cost - extra_target)
                    <= abs(larger_extra_cost - extra_target)
                    else larger_extra_cost
                )

            # Update the smallest difference and best cost
            total_cost = base_cost + closest_extra_cost
            diff = abs(total_cost - target)

            if diff < smallest_diff:
                smallest_diff = diff
                best_cost = total_cost
            elif diff == smallest_diff:
                # Always choose the smallest cost for the same
                # absolute difference
                best_cost = min(best_cost, total_cost)

        return best_cost


# @leet end
