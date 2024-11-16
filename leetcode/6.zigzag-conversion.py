# @leet start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Handle edge case of numRows == 1 here
        if numRows == 1:
            return s

        # Here with m = 2 * numRows - 2 and integer k >= 0, for row 0 we
        # include all valid indices
        #
        # s[mk];
        #
        # for row numRows - 1 we include all valid indices
        #
        # s[mk + numRows - 1];
        #
        # for row p with 0 < p < numRows - 1 we include all valid indices
        #
        # s[mk - p], s[mk + p].
        m = 2 * numRows - 2

        result = ""

        # Add to the results row by row
        for row in range(numRows):
            try:
                k = 0

                while True:
                    mk = m * k

                    # Add zigzag char for middle rows. The first element
                    # is always a non-zigzag char so we check for that
                    # here.
                    if 0 < row < numRows - 1 and mk != 0:
                        result += s[mk - row]

                    # Add non-zigzag char for all rows
                    result += s[mk + row]

                    k += 1
            except IndexError:
                pass

        return result


# @leet end
