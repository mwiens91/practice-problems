# @leet start
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        num_rows = len(strs)
        num_cols = len(strs[0])

        col_delete_count = 0

        for col in range(num_cols):
            prev_char = strs[0][col]

            for row in range(1, num_rows):
                if strs[row][col] < prev_char:
                    col_delete_count += 1

                    break

                prev_char = strs[row][col]

        return col_delete_count


# @leet end
