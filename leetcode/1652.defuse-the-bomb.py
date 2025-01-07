# @leet start
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        # Store result in separate array
        n = len(code)
        result = [0] * n

        # Get out if k == 0
        if k == 0:
            return result

        # Build up result
        for idx in range(n):
            sum_ = 0

            if k > 0:
                # Next k numbers
                range_ = range(idx + 1, idx + 1 + k)
            else:
                # Previous k numbers
                range_ = range(idx - 1, idx - 1 + k, -1)

            # Sum the numbers
            for sum_idx in range_:
                sum_ += code[sum_idx % n]

            result[idx] = sum_

        return result


# @leet end
