# @leet start
from collections import deque


class RecentCounter:

    def __init__(self):
        self.interval_length = 3000
        self.request_queue = deque()

    def ping(self, t: int) -> int:
        # Add the current request
        self.request_queue.append(t)

        # Flush any items that occured before the given interval
        print(self.request_queue[0], t - self.interval_length, self.request_queue[0] < t - self.interval_length)
        if self.request_queue[0] < t - self.interval_length:
            self.request_queue.popleft()

        # Return the number of items in the queue
        return len(self.request_queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @leet end
