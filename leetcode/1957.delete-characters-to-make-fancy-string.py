# @leet start
import re


class Solution:
    def makeFancyString(self, s: str) -> str:
        return re.sub(r"(.)\1{2,}", lambda m: m.group(1) * 2, s)


# @leet end
