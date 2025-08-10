# @leet start
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Compare the counts of digits in n with powers of 2
        # that contain the same number of digits as n
        n_str = str(n)
        target_digits = len(n_str)
        target_counter = Counter(n_str)

        i = 0

        while True:
            power_of_two_str = str(2**i)
            num_digits = len(power_of_two_str)

            if num_digits > target_digits:
                return False

            if (
                num_digits == target_digits
                and Counter(power_of_two_str) == target_counter
            ):
                return True

            i += 1


# @leet end
