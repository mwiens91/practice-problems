# @leet start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Get the string representation of num
        num_str = str(num)

        # Return the number of k-length substrings that divide num
        return sum(
            int(substr_int != 0 and num % substr_int == 0)
            for substr_int in (
                int(num_str[i : i + k]) for i in range(len(num_str) - k + 1)
            )
        )


# @leet end
