# @leet start
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # Assert that the list length is >= 3
        n = len(arr)

        if n < 3:
            return False

        # Assert that arr starts strictly increasing and switches to
        # strictly decreasing exactly once
        if arr[0] >= arr[1]:
            return False

        is_increasing = True

        for i in range(1, n - 1):
            # If any adjacent elements are equal or if we are increasing
            # but we've already switched to decreasing, arr cannot be a
            # mountain array
            if arr[i] == arr[i + 1] or arr[i] < arr[i + 1] and not is_increasing:
                return False

            # If we've just started decreasing, flip the is_increasing
            # flag to False
            if arr[i] > arr[i + 1] and is_increasing:
                is_increasing = False

        # If we end iteration and we're decreasing, arr is a mountain
        # array
        return not is_increasing


# @leet end
