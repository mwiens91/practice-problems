# @leet start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        CODE_POINT_A = ord("a")
        counts = [0] * 26

        for ch in magazine:
            counts[ord(ch) - CODE_POINT_A] += 1

        for ch in ransomNote:
            if not counts[ord(ch) - CODE_POINT_A]:
                return False

            counts[ord(ch) - CODE_POINT_A] -= 1

        return True


# @leet end
