# @leet start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        # Do a binary search
        left = 1
        right = n

        while True:
            mid = (left + right) // 2

            if guess(mid) == 0:
                return mid

            if guess(mid) == 1:
                # Mid is lower
                left = mid + 1
            else:
                # Mid is higher
                right = mid - 1


# @leet end
