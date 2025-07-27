# @leet start
class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:
        max_push_time = 0
        max_push_time_idx = 0
        prev_time = 0

        for idx, time in events:
            push_time = time - prev_time
            prev_time = time

            if push_time > max_push_time:
                max_push_time = push_time
                max_push_time_idx = idx
            elif push_time == max_push_time and idx < max_push_time_idx:
                max_push_time_idx = idx

        return max_push_time_idx


# @leet end
