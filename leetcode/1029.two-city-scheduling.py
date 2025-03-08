# @leet start
class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        # Sort the savings in descending order of savings
        costs.sort(key=lambda l: abs(l[0] - l[1]), reverse=True)

        # Greedily assign the person with the current largest savings to
        # their cheaper city if possible
        n = len(costs) // 2

        city_a_count = 0
        city_b_count = 0

        total_cost = 0

        for city_a_cost, city_b_cost in costs:
            # Assign to city A if it's cheaper and it's not full or if
            # city B is full; else assign to city B
            if city_a_cost <= city_b_cost and city_a_count < n or city_b_count == n:
                total_cost += city_a_cost
                city_a_count += 1
            else:
                total_cost += city_b_cost
                city_b_count += 1

        return total_cost


# @leet end
