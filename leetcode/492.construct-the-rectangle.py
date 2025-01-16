# @leet start
import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        # Find the minimum length. Can't really beat linear time here,
        # from what I can tell and from what I've searched up. I'm a
        # little surprised there's no fancy math tricks here, to be
        # honest.
        for length in range(math.ceil(math.sqrt(area)), area + 1):
            if area % length == 0:
                return [length, area // length]


# @leet end
