# @leet start
class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        # Call the original array R (short for result) and the encoded
        # array E. Since
        #
        # E_i = R_i ^ R_{i + 1}
        #
        # R_{i + 1}
        #   = R_{i + 1} ^ 0
        #   = R_{i + 1} ^ R_i ^ R_i
        #   = E_i ^ R_i
        result = [first]

        # Append the i + 1th element to result
        for e_i, r_i in zip(encoded, result):
            result.append(e_i ^ r_i)

        return result


# @leet end
