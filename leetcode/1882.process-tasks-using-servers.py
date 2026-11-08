# @leet start
import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Ready heap: (weight, index)
        # In use heap: (time when ready, weight, index)
        ready_heap: list[tuple[int, int]] = [
            (weight, i) for i, weight in enumerate(servers)
        ]
        heapq.heapify(ready_heap)
        in_use_heap: list[tuple[int, int, int]] = []

        res: list[int] = []
        time = 0

        def cycle_in_servers():
            while in_use_heap and in_use_heap[0][0] <= time:
                _, weight, server_idx = heapq.heappop(in_use_heap)
                heapq.heappush(ready_heap, (weight, server_idx))

        for task_idx, length in enumerate(tasks):
            time = max(time, task_idx)
            cycle_in_servers()

            if not ready_heap:
                time = in_use_heap[0][0]
                cycle_in_servers()

            weight, server_idx = heapq.heappop(ready_heap)
            res.append(server_idx)
            heapq.heappush(in_use_heap, (time + length, weight, server_idx))

        return res


# @leet end
