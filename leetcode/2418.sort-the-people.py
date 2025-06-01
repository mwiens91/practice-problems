# @leet start
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        heights, names = map(list, zip(*sorted(zip(heights, names), reverse=True)))

        return names


# @leet end
