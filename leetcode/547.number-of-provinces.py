# @leet start
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # For the first city 0, visit all cities directly or indirectly
        # connected to it until we exhaust all connections. Increment
        # the number of provinces by one. Then, for each city 1 to
        # n - 1, perform the same operation so long as we haven't
        # already visited the city.
        num_provinces = 0

        visited_set: set[int] = set()

        def explore_province(start_city_idx: int) -> None:
            nonlocal num_provinces

            # Get out if we've already explored this province
            if start_city_idx in visited_set:
                return

            # Add the starting city to the visited set
            visited_set.add(start_city_idx)

            # Explore all cities in the province
            city_queue = deque([start_city_idx])

            while city_queue:
                city_idx = city_queue.pop()

                for connected_city_idx, is_connected in enumerate(
                    isConnected[city_idx]
                ):
                    if is_connected and connected_city_idx not in visited_set:
                        city_queue.appendleft(connected_city_idx)
                        visited_set.add(connected_city_idx)

            num_provinces += 1

        # Visit each province
        for city_idx in range(len(isConnected)):
            explore_province(city_idx)

        return num_provinces


# @leet end
