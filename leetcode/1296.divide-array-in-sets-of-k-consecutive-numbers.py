# @leet start
class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if k == 1:
            return True

        if len(nums) % k != 0:
            return False

        counts: dict[int, int] = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in sorted(counts.keys()):
            for _ in range(counts[num]):
                j = 1

                while j < k:
                    if num + j not in counts or counts[num + j] == 0:
                        return False

                    counts[num + j] -= 1
                    j += 1

        return True


# @leet end
