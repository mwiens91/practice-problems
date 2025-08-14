# @leet start
class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        start_col = s[0]
        start_row = int(s[1])

        max_col_delta = ord(s[3]) - ord(start_col)
        max_row_delta = int(s[4]) - start_row

        result: list[str] = []

        for col_delta in range(max_col_delta + 1):
            this_col = chr(ord(start_col) + col_delta)

            for row_delta in range(max_row_delta + 1):
                result.append(f"{this_col}{start_row + row_delta}")

        return result


# @leet end
