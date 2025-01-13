# @leet start
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        ball_indices = [i for i, x in enumerate(boxes) if x == "1"]

        return [
            sum(abs(ball_idx - i) for ball_idx in ball_indices)
            for i in range(len(boxes))
        ]


# @leet end
