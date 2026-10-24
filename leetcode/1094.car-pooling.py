# @leet start
import heapq
from operator import itemgetter


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=itemgetter(1))
        heap: list[tuple[int, int]] = []
        curr_passengers = 0

        for num_passengers, src, dst in trips:
            while heap and heap[0][0] <= src:
                _, remove_passengers = heapq.heappop(heap)
                curr_passengers -= remove_passengers

            curr_passengers += num_passengers

            if curr_passengers > capacity:
                return False

            heapq.heappush(heap, (dst, num_passengers))

        return True


# @leet end
