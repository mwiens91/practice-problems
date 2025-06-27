# @leet start
class Solution:
    def minimumSum(self, num: int) -> int:
        digit_list = sorted(map(int, str(num)))

        return 10 * (digit_list[0] + digit_list[1]) + digit_list[2] + digit_list[3]


# @leet end
