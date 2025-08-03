# @leet start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        result_count = 0

        for i in range(n):
            zeros_count = 0
            ones_count = 0

            for j in range(i, n):
                if s[j] == "0":
                    zeros_count += 1
                else:
                    ones_count += 1

                if zeros_count <= k or ones_count <= k:
                    result_count += 1
                else:
                    break

        return result_count


# @leet end
