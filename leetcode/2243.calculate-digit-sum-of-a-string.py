# @leet start
import math


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        new_s_list: list[str] = []

        while len(s) > k:
            for i in range(math.ceil(len(s) / k)):
                # Get digits, sum them, and convert to string to be joined
                # into the new s
                new_s_list.append(str(sum(map(int, s[i * k : (i + 1) * k]))))

            s = "".join(new_s_list)
            new_s_list = []

        return s


# @leet end
