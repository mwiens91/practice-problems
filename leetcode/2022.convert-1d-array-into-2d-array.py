# @leet start
class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        num_1d_elems = len(original)

        if num_1d_elems != m * n:
            return []

        result: list[list[int]] = []

        for row_num in range(m):
            result.append(original[row_num * n : (row_num + 1) * n])

        return result


# @leet end
