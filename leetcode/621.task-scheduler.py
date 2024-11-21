# @leet start
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Get the negatives of the count of each task and put them in a
        # heap. We want the negative of the count because we're going to
        # have a max heap of the counts of each task, but the heapq
        # algorithms work on min heaps, so the value heapq operates on
        # needs to be negated while it's in the heap. Note that we don't
        # need to care about what the task actually is, just the count.
        heap = [-count for _, count in Counter(tasks).items()]

        heapq.heapify(heap)

        # Keep track of time
        t = 0

        # Keep a queue of things to add to the heap at time t. Elements
        # of the queue will hold tuples (time to add to heap, -count).
        # Also, we're using a deque because its simpler than Python's
        # queue library from my (limited) experience; we'll just use it
        # as a queue though.
        add_to_heap_queue = deque()

        QUEUE_TIME_INDEX = 0
        QUEUE_COUNT_INDEX = 1

        while heap or add_to_heap_queue:
            # Increment time
            t += 1

            # Add new elements to the heap if it's time to add them
            while add_to_heap_queue and t == add_to_heap_queue[-1][QUEUE_TIME_INDEX]:
                heapq.heappush(heap, add_to_heap_queue.pop()[QUEUE_COUNT_INDEX])

            # Get an element from the heap and schedule to add it again
            # (with a reduced count) later
            if heap:
                smallest_negative_count = heapq.heappop(heap)

                # If the negative count is at -1, this is the final
                # instance of the task, so we don't need to schedule
                # more
                if smallest_negative_count < -1:
                    # The time the task is next available is immediately
                    # after the current time (t) + the gap time (n): so
                    # it's t + n + 1
                    add_to_heap_queue.appendleft((t + n + 1, smallest_negative_count + 1))


        return t


# @leet end
