# @leet start
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Store results in this
        results = [None] * len(score)

        # Make a list containing tuples (score_, idx) for every element
        # in score and sort it.
        sorted_scores = sorted(
            [(score_, idx) for idx, score_ in enumerate(score)], reverse=True
        )

        for rank, (_, idx) in enumerate(sorted_scores, 1):
            rank_str = str(rank)

            if rank == 1:
                rank_str = "Gold Medal"
            elif rank == 2:
                rank_str = "Silver Medal"
            elif rank == 3:
                rank_str = "Bronze Medal"

            results[idx] = rank_str

        return results


# @leet end
