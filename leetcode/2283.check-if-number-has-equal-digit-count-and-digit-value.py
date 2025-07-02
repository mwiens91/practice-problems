# @leet start
class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(num_i) for i, num_i in enumerate(num))


# @leet end
