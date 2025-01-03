# @leet start
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # First sort the numbers
        arr.sort()

        # Find minimum absolute difference
        n = len(arr)
        min_abs_diff = arr[1] - arr[0]

        for i in range(1, n - 1):
            min_abs_diff = min(min_abs_diff, arr[i + 1] - arr[i])

        # Get all pairs with this absolute difference
        pairs = []

        for i in range(n - 1):
            if arr[i + 1] - arr[i] == min_abs_diff:
                pairs.append([arr[i], arr[i + 1]])

        return pairs


# @leet end
