# @leet start
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False

        counts: dict[int, int] = {}

        for num in hand:
            counts[num] = counts.get(num, 0) + 1

        for i, num in enumerate(sorted(counts.keys())):
            for _ in range(counts[num]):
                j = 1

                while j < groupSize:
                    if num + j not in counts or counts[num + j] == 0:
                        return False

                    counts[num + j] -= 1
                    j += 1

        return True


# @leet end
