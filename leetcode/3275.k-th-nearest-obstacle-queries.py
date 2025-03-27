# @leet start
import heapq


class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        # We'll maintain a max-heap of max size k containing Manhattan
        # distances from the origin. Since Python's heapq uses
        # min-heaps, we store the negative of numbers in the heap.
        heap = []
        results = []

        for x, y in queries:
            # First, push the distance to the heap, maintaining at most
            # k elements in the heap. Then either append -1 to the
            # results list if there are less than k elements in the
            # heap, or negate the most negative number and append it to
            # the results list if there are k elements in the heap.
            distance = abs(x) + abs(y)

            heap_size = len(heap)

            if heap_size < k - 1:
                heapq.heappush(heap, -distance)
                results.append(-1)
            elif heap_size == k - 1:
                heapq.heappush(heap, -distance)
                results.append(heap[0])
            else:
                # heap_size == k
                heapq.heappushpop(heap, -distance)
                results.append(heap[0])

        return results


# @leet end
