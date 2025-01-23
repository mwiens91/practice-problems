# @leet start
class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # Sort the array, then make sure the differences between
        # successive elements are the same
        arr.sort()

        first_difference = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != first_difference:
                return False

        return True


# @leet end
