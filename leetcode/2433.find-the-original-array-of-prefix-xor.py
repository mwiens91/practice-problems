# @leet start
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        return [pref[0]] + [pref[i - 1] ^ pref[i] for i in range(1, len(pref))]


# @leet end
