# @leet start
from operator import itemgetter


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=itemgetter(k), reverse=True)


# @leet end
