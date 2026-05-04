# @leet start
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for num1, num2 in zip_longest(
            self.get_components(version1), self.get_components(version2), fillvalue=0
        ):
            if num1 < num2:
                return -1

            if num1 > num2:
                return 1

        return 0

    def get_components(self, v: str) -> list[int]:
        res: list[int] = []

        left = 0
        right = 0

        while right < len(v):
            if v[right] == ".":
                res.append(int(v[left:right]))
                left = right + 1
                right += 2
            else:
                right += 1

        res.append(int(v[left:right]))

        return res


# @leet end
