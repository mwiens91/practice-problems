# @leet start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CODE_PT_A = ord("a")
        counts = [0] * 26

        for ch in s:
            counts[ord(ch) - CODE_PT_A] += 1

        for ch in t:
            counts[ord(ch) - CODE_PT_A] -= 1

        for count in counts:
            if count != 0:
                return False

        return True


# @leet end
