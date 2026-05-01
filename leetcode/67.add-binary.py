# @leet start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res: list[str] = []
        carry = 0

        for i in range(max(len(a), len(b))):
            dig_sum = carry

            if i < len(a):
                dig_sum += int(a[-1 - i])

            if i < len(b):
                dig_sum += int(b[-1 - i])

            res.append(str(dig_sum % 2))
            carry = dig_sum // 2

        if carry:
            res.append("1")

        return "".join(res[::-1])


# @leet end
