# @leet start
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result: list[int] = [0] * n
        current = 1

        for i in range(n):
            result[i] = current

            if 10 * current <= n:
                current *= 10
            else:
                while current % 10 == 9 or current >= n:
                    current //= 10

                current += 1

        return result


# @leet end
