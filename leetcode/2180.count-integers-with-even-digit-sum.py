# @leet start
class Solution:
    def countEven(self, num: int) -> int:
        def get_digit_sum(x: int) -> int:
            return sum(map(int, str(x)))

        return sum(1 for x in range(1, num + 1) if get_digit_sum(x) % 2 == 0)


# @leet end
