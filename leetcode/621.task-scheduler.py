# @leet start
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        CODE_POINT_A = ord("A")

        max_count = 0
        num_with_max_count = 0
        counts = [0] * 26

        for task in tasks:
            idx = ord(task) - CODE_POINT_A
            counts[idx] += 1

            if counts[idx] == max_count:
                num_with_max_count += 1
            elif counts[idx] > max_count:
                max_count += 1
                num_with_max_count = 1

        return max(len(tasks), num_with_max_count - 1 + max_count + n * (max_count - 1))


# @leet end
