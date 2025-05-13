# @leet start
class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        INCREASE = "I"
        # DECREASE = "D"

        # Start with 0 as the first integer. If we need to increase, use
        # the next available positive integer; if we need to decrease
        # use the next available negative integer. Then shift all
        # integers so that they are non-negative.
        next_available_positive = 1
        next_available_negative = -1

        result = [0]

        for direction in s:
            if direction == INCREASE:
                result.append(next_available_positive)
                next_available_positive += 1
            else:
                result.append(next_available_negative)
                next_available_negative -= 1

        # Shift
        shift = -next_available_negative - 1

        return [x + shift for x in result]


# @leet end
