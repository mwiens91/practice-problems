# @leet start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Greedy solution: increment a balanced substring count whenever
        # the number of Ls equals the number of Rs
        num_Ls = 0
        num_Rs = 0

        num_balanced_substrings = 0

        for char in s:
            if char == "L":
                num_Ls += 1
            else:
                num_Rs += 1

            if num_Ls == num_Rs:
                num_balanced_substrings += 1

        return num_balanced_substrings


# @leet end
