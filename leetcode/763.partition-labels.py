# @leet start
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # For each letter, find its last index
        last_idx_dict = {}

        for i, char in enumerate(s):
            last_idx_dict[char] = i

        # Find the maximum number of partitions
        partition_lengths: list[int] = []

        current_start_idx = 0
        current_end_idx = last_idx_dict[s[0]]

        n = len(s)
        i = 0

        while i < n:
            current_end_idx = max(current_end_idx, last_idx_dict[s[i]])

            if i == current_end_idx:
                partition_lengths.append(current_end_idx - current_start_idx + 1)

                current_start_idx = i + 1

            i += 1

        return partition_lengths


# @leet end
