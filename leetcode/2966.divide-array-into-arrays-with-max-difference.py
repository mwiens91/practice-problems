# @leet start
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        # Be greedy: sort the numbers and then divide into n / 3
        # subarrays of size 3
        nums.sort()

        n = len(nums)
        subarrays: list[list[int]] = []

        for i in range(n // 3):
            subarray = nums[i * 3 : (i + 1) * 3]

            # Validate subarray. If it's invalid, return an empty list
            if subarray[-1] - subarray[0] > k:
                return []

            subarrays.append(subarray)

        return subarrays


# @leet end
