# @leet start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # For each integer with an even number of digits, see if it's
        # symmetric. Because the bounds on low and high aren't large, we
        # don't save much by trying to reuse results, so we'll just
        # compute the solution fresh for each number.
        num_symmetric_ints = 0

        for num in range(low, high + 1):
            digits = [int(x) for x in str(num)]

            n = len(digits)

            if n % 2 == 0 and sum(digits[: n // 2]) == sum(digits[n // 2 :]):
                num_symmetric_ints += 1

        return num_symmetric_ints


# @leet end
