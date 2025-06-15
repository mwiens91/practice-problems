# @leet start
class Solution:
    def addDigits(self, num: int) -> int:
        # This is a number theory trick: look up "digital root". The sum
        # of a numbers digit is congruent to the number itself mod
        # 9. The -1,+1 is so that for multiples of 9, we have an answer
        # of 9, not 0.
        return 0 if num == 0 else (num - 1) % 9 + 1


# @leet end
