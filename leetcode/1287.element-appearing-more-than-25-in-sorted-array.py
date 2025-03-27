# @leet start
class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        # Because the target number spans more than 25% of the sorted
        # array it must be in one of indices 0, n // 4 - 1,
        # 2 * (n // 4) - 1, 3 * (n // 4) - 1, 4 * (n // 4) - 1. Note
        # that because the target number must be unique, the length of
        # arr is either
        #
        # - 1, for which only the first and last target indices are
        # valid, but in the actual code only the first index is
        # evaluated so this isn't an issue
        # - >= 4, in which case all target indices are valid
        n = len(arr)

        target_idxs = [0, n // 4 - 1, 2 * n // 4 - 1, 3 * n // 4 - 1, 4 * n // 4 - 1]

        # For each target, find their count
        for target_idx in target_idxs:
            target = arr[target_idx]

            # Find first occurance of target
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            first_idx = left

            # Find last occurance of target
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            last_idx = right

            if last_idx - first_idx + 1 > n // 4:
                return target


# @leet end
