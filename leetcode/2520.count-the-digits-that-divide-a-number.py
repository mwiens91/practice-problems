# @leet start
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0

        # We'll repeatedly divide the number by 10 while obtaining its
        # digits
        remaining_num = num

        while remaining_num:
            # See if the current digit divides num
            if num % (remaining_num % 10) == 0:
                count += 1

            remaining_num //= 10

        return count


# @leet end
