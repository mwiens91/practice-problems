# @leet start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Add one starting from most to least significant digit until
        # there is no carry-digit
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break

            digit_sum = digits[i] + carry

            # Modify digits list and update carry
            digits[i] = digit_sum % 10
            carry = digit_sum // 10

        # If there is still a carry, we need to prepend it to the list
        if carry:
            return [carry] + digits

        return digits


# @leet end
