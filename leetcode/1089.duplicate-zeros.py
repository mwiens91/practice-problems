# @leet start
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        # Calculate the number of elements we need to shift the last
        # element in the final result forward by
        i = 0
        shift = 0

        while i + shift < n:
            if arr[i] == 0:
                shift += 1

            i += 1

        # Move the pointer back to the last element in the final result
        i -= 1

        # Move each element forward by the appropriate shift and
        # duplicate any 0s
        while i >= 0:
            if arr[i] == 0:
                shift -= 1

                arr[i + shift] = 0

                try:
                    arr[i + shift + 1] = 0
                except IndexError:
                    pass
            else:
                arr[i + shift] = arr[i]

            i -= 1


# @leet end
