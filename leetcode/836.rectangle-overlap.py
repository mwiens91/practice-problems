# @leet start
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return (
            rec2[0] < rec1[2]  # rec2 starts before rec1 ends horizontally
            and rec1[0] < rec2[2]  # rec1 starts before rec2 ends horizontally
            and rec2[1] < rec1[3]  # same as above but for vertical
            and rec1[1] < rec2[3]
        )


# @leet end
