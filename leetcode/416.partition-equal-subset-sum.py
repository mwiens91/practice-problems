# @leet start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        sums = {0}

        for num in nums:
            new_sums: set[int] = set()

            for sum_ in sums:
                new_sum = num + sum_

                if new_sum == target:
                    return True

                if new_sum < target:
                    new_sums.add(new_sum)

            sums.update(new_sums)

        return False


# @leet end
