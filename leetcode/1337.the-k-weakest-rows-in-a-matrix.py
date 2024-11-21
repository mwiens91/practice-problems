# @leet start
import heapq


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # Get number of soldiers per row and put it in a min heap.
        # Elements of the min heap will have (num_soldiers, row_idx)
        # values.
        num_rows = len(mat)
        num_cols = len(mat[0])

        heap = []

        for i in range(num_rows):
            count = 0

            for j in range(num_cols):
                if mat[i][j] == 0:
                    # No more soldiers
                    break

                count += 1

            heap.append((count, i))

        heapq.heapify(heap)

        # Get the row index of the first k elements of the heap
        results = []

        for _ in range(k):
            results.append(heapq.heappop(heap)[1])

        return results


# @leet end
