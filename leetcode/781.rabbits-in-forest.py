# @leet start
from collections import Counter
import math


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        # Note that a single response of x implies there are at least
        # x + 1 rabbits in the forest. If there are m counts of response
        # x, then there must be at least y = ceil(m / (x + 1)) unique
        # colours corresponding to the response x, and thus at least
        # y * (x + 1) rabbits in the forest due to this response. So we
        # simply need to sum this formula for each unique response.
        response_counts = Counter(answers)

        min_rabbits_in_forest = 0

        for response, count in response_counts.items():
            num_per_group = response + 1
            min_rabbits_in_forest += math.ceil(count / num_per_group) * num_per_group

        return min_rabbits_in_forest


# @leet end
