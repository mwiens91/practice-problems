# @leet start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result: list[int] = []

        for x in range(left, right + 1):
            remaining_x = x

            while remaining_x:
                digit = remaining_x % 10

                if digit == 0 or x % digit != 0:
                    break

                remaining_x //= 10
            else:
                result.append(x)

        return result


# @leet end
