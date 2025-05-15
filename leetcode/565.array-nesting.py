# @leet start
class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        # Idea: find the longest cycle
        visited_idxs: set[int] = set()

        longest_cycle = 1

        for i in range(len(nums)):
            if i in visited_idxs:
                continue

            # Traverse the cycle
            current_idx = i
            cycle_visited_idxs = set([current_idx])

            while nums[current_idx] not in cycle_visited_idxs:
                current_idx = nums[current_idx]
                cycle_visited_idxs.add(current_idx)

            # Update the longest cycle and add to cycle indices to the
            # visited indices set
            longest_cycle = max(longest_cycle, len(cycle_visited_idxs))

            visited_idxs.update(cycle_visited_idxs)

        return longest_cycle


# @leet end
