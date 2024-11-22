# @leet start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Get an upper bound on the outputs number of digits
        n1 = len(num1)
        n2 = len(num2)

        max_output_digits = n1 + n2 + 2

        # Convert the strings into a list of integers
        num1_ints = [int(x) for x in num1]
        num2_ints = [int(x) for x in num2]

        # Store our result in this, we'll convert the integers to
        # strings later and then stitch together the strings while
        # leaving off any leading 0s
        result = [0] * max_output_digits

        # Using the method of multiplication I was taught in primary
        # school, num1 will be the bottom number and num2 will be the
        # top number. We're not going to bother with carryover digits
        # though. We'll handle those in an alternate way later.
        for i1 in range(n1):
            digit_1 = num1_ints[-(i1 + 1)]

            for i2 in range(n2):
                digit_2 = num2_ints[-(i2 + 1)]

                result[-(i1 + i2 + 1)] += digit_1 * digit_2

        # Now handle carryovers all at once
        for i in range(max_output_digits - 1, -1, -1):
            carryover = result[i] // 10
            remainder = result[i] % 10

            result[i] = remainder
            result[i - 1] += carryover

        # Convert to string and return
        start_idx = 0

        # First, skip leading 0s: we need to deal with the edge case
        # where the result is identically 0 here
        while start_idx < max_output_digits and result[start_idx] == 0:
            start_idx += 1

        if start_idx == max_output_digits:
            # Identically 0
            return "0"

        return "".join([str(x) for x in result[start_idx:]])


# @leet end
