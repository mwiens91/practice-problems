# @leet start
from collections import defaultdict


class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        counts: defaultdict[str, int] = defaultdict(int)

        for response_list in responses:
            for distinct_response in set(response_list):
                counts[distinct_response] += 1

        return min(counts.items(), key=lambda x: (-x[1], x[0]))[0]


# @leet end
