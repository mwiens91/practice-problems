# @leet start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        score = nums[0] + nums[1]
        count = 1

        for i in range(2, (n // 2) * 2, 2):
            if nums[i] + nums[i + 1] == score:
                count += 1
            else:
                return count

        return count


# @leet end
