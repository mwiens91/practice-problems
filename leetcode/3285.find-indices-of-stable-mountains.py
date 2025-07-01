# @leet start
class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        result: list[int] = []

        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                result.append(i)

        return result


# @leet end
