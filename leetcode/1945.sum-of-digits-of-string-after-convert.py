# @leet start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert characters in string to integers
        code_point_a = ord("a")
        s_nums = [ord(char) - code_point_a + 1 for char in s]

        # Split integers into their digits
        s_digits: list[int] = []

        for num in s_nums:
            if num > 9:
                s_digits.extend([num // 10, num % 10])
            else:
                s_digits.append(num)

        # Sum digits k times
        while k > 0 and len(s_digits) > 1:
            s_int = sum(s_digits)

            # Set up for next iteration
            k -= 1
            s_digits = list(map(int, str(s_int)))

        # Return final number
        if len(s_digits) == 1:
            return s_digits[0]

        # If the above condition is False, we've entered the above loop
        # at least s_int will exist
        return s_int


# @leet end
