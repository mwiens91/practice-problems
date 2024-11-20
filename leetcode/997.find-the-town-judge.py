# @leet start
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Count how many people each person trusts and how many people
        # trust each person
        trusts_others_counts = {x: 0 for x in range(1, n + 1)}
        trusts_self_counts = {x: 0 for x in range(1, n + 1)}

        for self_, other in trust:
            trusts_others_counts[self_] += 1
            trusts_self_counts[other] += 1

        # Now see if there's a judge
        for town_id in range(1, n + 1):
            if (
                trusts_others_counts[town_id] == 0
                and trusts_self_counts[town_id] == n - 1
            ):
                return town_id

        return -1


# @leet end
