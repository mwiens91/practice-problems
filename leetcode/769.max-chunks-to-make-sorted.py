# @leet start
class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)

        count = 0
        end = 0

        for i in range(n):
            if arr[i] == n - 1:
                return count + 1

            if arr[i] > end:
                end = arr[i]
            elif i == end:
                count += 1
                end += 1


# @leet end
