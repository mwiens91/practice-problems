# @leet start
class Solution:
    def buildArray(
        self, target: list[int], n: int  # pylint: disable=unused-argument
    ) -> list[str]:
        result: list[str] = []

        prev_num = 0

        for num in target:
            result.extend(["Push", "Pop"] * (num - prev_num - 1))
            result.append("Push")

            prev_num = num

        return result


# @leet end
