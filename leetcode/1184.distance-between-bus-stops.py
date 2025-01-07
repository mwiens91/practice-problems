# @leet start
class Solution:
    def distanceBetweenBusStops(
        self, distance: list[int], start: int, destination: int
    ) -> int:
        first = min(start, destination)
        second = max(start, destination)

        return min(
            sum(distance[first : second]),
            sum(distance[:first]) + sum(distance[second:]),
        )


# @leet end
