# @leet start
class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # The following function to rotate a square matrix is taken from
        # my solution to LC 48. The solution there has comments, which
        # I've stripped out here.
        def rotate_matrix(matrix: list[list[int]]) -> None:
            n = len(matrix)

            def rotate_edge(m: int) -> None:
                tl_idx = (n - m) // 2
                br_idx = n - tl_idx - 1

                for i in range(m - 1):
                    (
                        matrix[tl_idx][tl_idx + i],
                        matrix[tl_idx + i][br_idx],
                        matrix[br_idx][br_idx - i],
                        matrix[br_idx - i][tl_idx],
                    ) = (
                        matrix[br_idx - i][tl_idx],
                        matrix[tl_idx][tl_idx + i],
                        matrix[tl_idx + i][br_idx],
                        matrix[br_idx][br_idx - i],
                    )

            m = n

            while m >= 2:
                rotate_edge(m)

                m -= 2

        if mat == target:
            return True

        for _ in range(3):
            rotate_matrix(target)

            if mat == target:
                return True

        return False


# @leet end
