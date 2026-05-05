# @leet start
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        curr = [0, 0, 0]
        idxs = range(3)

        for trip in triplets:
            if any(trip[i] == target[i] for i in idxs) and all(
                trip[i] <= target[i] for i in idxs
            ):
                curr = [max(trip[i], curr[i]) for i in idxs]

                if all(curr[i] == target[i] for i in idxs):
                    return True

        return False


# @leet end
