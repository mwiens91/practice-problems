# @leet start
class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False

        for char in s:
            if char == "a":
                if seen_b:
                    return False
            else:
                seen_b = True

        return True


# @leet end
