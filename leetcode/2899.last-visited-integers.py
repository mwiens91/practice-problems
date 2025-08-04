# @leet start
class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        minus_one_run = 0

        seen: list[int] = []
        ans: list[int] = []

        for num in nums:
            if num == -1:
                minus_one_run += 1

                if minus_one_run <= len(seen):
                    ans.append(seen[-minus_one_run])
                else:
                    ans.append(-1)
            else:
                minus_one_run = 0
                seen.append(num)

        return ans


# @leet end
