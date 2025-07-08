# @leet start
class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        return max(int(str) if str.isdigit() else len(str) for str in strs)


# @leet end
