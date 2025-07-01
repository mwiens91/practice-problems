# @leet start
class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        nums_seen: set[int] = set()
        result: list[int] = []

        for num in nums:
            if num in nums_seen:
                result.append(num)
            else:
                nums_seen.add(num)

        return result


# @leet end
