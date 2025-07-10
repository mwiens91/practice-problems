# @leet start
class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum(1 for detail in details if detail[11:13] > "60")


# @leet end
