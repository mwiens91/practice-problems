# @leet start
import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        # Sort by ascending start date
        events.sort()

        # Keep events that have already started in a heap
        events_attended = 0
        current_day = 1
        heap: list[int] = []

        i = 0
        n = len(events)

        while heap or i < n:
            # Skip events that have already ended
            while heap and heap[0] < current_day:
                heapq.heappop(heap)

            # If the heap is empty and there are more events left, skip
            # to the start day of the next event and add it to the
            # heap
            if not heap and i < n:
                current_day = events[i][0]
                heap.append(events[i][1])
                i += 1

            # Add events starting on the current day to the heap
            while i < n and events[i][0] == current_day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Consume an event
            if heap:
                heapq.heappop(heap)
                events_attended += 1
                current_day += 1

        return events_attended


# @leet end
