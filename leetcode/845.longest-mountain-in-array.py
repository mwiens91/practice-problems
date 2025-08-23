# @leet start
class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        best = 0

        start = 0

        while start < n - 2:
            i = start

            # Check that we can ascend
            if arr[i] >= arr[i + 1]:
                start = i + 1
                continue

            # Ascend as much as possible
            while i < n - 1 and arr[i] < arr[i + 1]:
                i += 1

            # Check that we can descend
            if i >= n - 1 or arr[i] == arr[i + 1]:
                start = i + 1
                continue

            # Descend as much as possible
            while i < n - 1 and arr[i] > arr[i + 1]:
                i += 1

            best = max(best, i - start + 1)
            start = i

        return best


# @leet end
