# @leet start
class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        best_idx = -1
        best_cap = 101

        for i, cap in enumerate(capacity):
            if itemSize <= cap < best_cap:
                best_idx = i
                best_cap = cap

        return best_idx


# @leet end
