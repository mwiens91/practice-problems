# @leet start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Find first odd digit from the end, and return the substring
        # with that as the last digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[: i + 1]

        # No odd digits
        return ""


# @leet end
