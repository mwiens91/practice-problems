# @leet start
class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        # NOTE: could add a quick check to see if k % num_cols == 0:
        # answer is always True in that case
        num_cols = len(mat[0])

        for row in mat:
            for i in range(num_cols):
                if row[i] != row[(i + k) % num_cols]:
                    return False

        return True


# @leet end
