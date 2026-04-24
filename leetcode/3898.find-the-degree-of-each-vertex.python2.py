# @leet start
class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        res = [0] * n

        for row in range(n):
            for col in range(row + 1, n):
                res[row] += matrix[row][col]
                res[col] += matrix[row][col]

        return res


# @leet end
