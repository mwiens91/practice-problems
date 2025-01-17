# @leet start
class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        # Loop over the (exclusive) end index y of the subarray
        # arr[y - m: y] we need to repeat k times. The end of the range
        # n - (k - 1) * m + 1 is chosen so that we can repeat the
        # subarray another k - 1 times without going out of bounds.
        for subarray_end_idx in range(m, len(arr) - (k - 1) * m + 1):
            subarray = arr[subarray_end_idx - m : subarray_end_idx]

            for i in range(k - 1):
                if (
                    subarray
                    != arr[subarray_end_idx + m * i : subarray_end_idx + m * (i + 1)]
                ):
                    # Subarray does not repeat k times
                    break
            else:
                # Subarray does repeat k times
                return True

        return False


# @leet end
