# @leet start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # The following is a procedure for adding two positive numbers.
        # Define stable_digits = a ^ b. This represents, in
        # pencil-and-paper addition, the digits in addition that aren't
        # carry over digits. Suppose, in their binary reprentations
        #
        # a = 011
        # b = 111
        #
        # In this example, the binary representation of the stable
        # digits would be
        #
        # stable_digits = a ^ b = 100
        #
        # Define carry_digits = (a & b) << 1. This represents the carry
        # over digits. In this example, we would have
        #
        # carry_digits = (a & b) << 1 = (011) << 1 = (110)
        #
        # We can find the sum of a and b by repeating this process with
        # a = stable_digits, b = carry_digits until the carry digits (b)
        # are 0.
        #
        # If one or both of a and b are negative and are represented
        # with two's complement, however, we need a modification (which
        # also works if a and b are positive):
        #
        # stable_digits = (a ^ b) & 0xFFF
        #
        # Here 0xFFF represents the maximum value of an unsigned 12 bit
        # integer. We need this mask because Python uses a
        # variable-length representation of integers; bitwise &ing with
        # the mask allows us to simulate the behaviour of fixed-width
        # integers.
        #
        # I chose 0xFFF because |a + b| <= 4095 = 0xFFF given the
        # constraints; however, using the maximum value of any unsigned
        # x bit integer for x >= 12 would work as well.
        MAX_UNSIGNED_INT = 0xFFF
        MAX_SIGNED_INT = 0x7FF

        while b != 0:
            a, b = (a ^ b) & MAX_UNSIGNED_INT, (a & b) << 1

        # Return the answer. a will be represented as an unsigned
        # integer, but if it has a negative bit, we convert it to its
        # proper signed representation.
        return a if a <= MAX_SIGNED_INT else ~(a ^ MAX_UNSIGNED_INT)


# @leet end
