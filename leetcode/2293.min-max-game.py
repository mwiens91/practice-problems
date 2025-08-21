# @leet start
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_length = len(nums) // 2
            new_nums = [0] * new_length

            for i in range(new_length):
                new_nums[i] = (min if i % 2 == 0 else max)(nums[2 * i], nums[2 * i + 1])

            nums = new_nums

        return nums.pop()


# @leet end
