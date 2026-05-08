# @leet start
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        def count_le(x: int) -> int:
            count = 0
            row = n - 1

            for col in range(n):
                while row >= 0 and matrix[row][col] > x:
                    row -= 1

                count += row + 1

            return count

        low = matrix[0][0]
        high = matrix[-1][-1]

        while low <= high:
            mid = (low + high) // 2

            if count_le(mid) >= k:
                high = mid - 1
            else:
                low = mid + 1

        return low


# @leet end
