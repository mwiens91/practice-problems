# @leet start
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_from_right = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_from_right = max_from_right, max(max_from_right, arr[i])

        return arr


# @leet end
