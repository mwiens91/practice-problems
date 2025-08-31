# @leet start
class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        friends_set = set(friends)

        return [x for x in order if x in friends_set]


# @leet end
