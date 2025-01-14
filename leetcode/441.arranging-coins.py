# @leet start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Recall that the sum of the first n digits is (n + 1) n / 2.
        # We'll do a binary search to find the largest k such that
        # (k + 1) k / 2 <= n.
        left = 1
        right = n

        best_k_found = 1

        while left <= right:
            k = (left + right) // 2
            sum_of_first_k_nums = (k + 1) * k // 2

            if sum_of_first_k_nums == n:
                return k

            if sum_of_first_k_nums < n:
                # Update best k found
                best_k_found = max(best_k_found, k)

                left = k + 1
            else:
                # sum_of_first_k_nums > n
                right = k - 1

        return best_k_found


# @leet end
