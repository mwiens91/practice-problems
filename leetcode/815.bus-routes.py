# @leet start
from collections import deque


FAILURE = -1


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        # Make the stops to route number dictionary. Stops are keys and
        # the corresponding values are lists of route numbers that go to
        # a given stop.
        stop_routes_dict = {}

        for route_number, route in enumerate(routes):
            for stop in route:
                if stop in stop_routes_dict:
                    stop_routes_dict[stop].append(route_number)
                else:
                    stop_routes_dict[stop] = [route_number]

        # Handle edge case: source is target
        if source == target:
            return 0

        # Handle edge case: source does not belong to a route
        if source not in stop_routes_dict:
            return FAILURE

        # Create a set for stops we've seen already (either already
        # visisted or planning to visit); a set for routes we've already
        # been on; and a deque to push stops, each element containing a
        # 2-tuple (stop, distance).
        seen_stop_set = {source}
        seen_route_set = set()
        next_deque = deque([(source, 0)])

        # We'll do a BFS to find the shortest distance
        while next_deque:
            # Grab a stop from the deque
            stop, distance = next_deque.pop()

            # Return the distance if we've reached the target
            if stop == target:
                return distance

            # Push all next stops to visit on the deque
            for route_number in stop_routes_dict[stop]:
                if route_number in seen_route_set:
                    continue

                for stop in routes[route_number]:
                    if stop not in seen_stop_set:
                        # Push to next_deque
                        next_deque.appendleft((stop, distance + 1))

                        # Never visit this stop again
                        seen_stop_set.add(stop)

                # Never go on this route again
                seen_route_set.add(route_number)

        return FAILURE


# @leet end
