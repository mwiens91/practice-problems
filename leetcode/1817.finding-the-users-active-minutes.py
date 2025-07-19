# @leet start
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        uam_dict: defaultdict[int, set[int]] = defaultdict(set)

        for user, time in logs:
            uam_dict[user].add(time)

        answer = [0] * k

        for times_set in uam_dict.values():
            total_minutes = len(times_set)

            if 1 <= total_minutes <= k:
                answer[total_minutes - 1] += 1

        return answer


# @leet end
