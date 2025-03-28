# @leet start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # We work only with positive n, so if n is negative, set x to
        # the reciprocal of x and negate n
        if n < 0:
            x = 1 / x
            n = -n

        # Suppose n is an exact power of 2. Then
        # x^n = (x^2)^(n/2) = ((x^2)^2)^(n/4) = ... = (...)^1
        # where the sum of 2s in the (...) of the right hand side is
        # equal to n. This results in log2(n) multiplications.
        #
        # Now suppose n is not an exact power of 2. Then, if n = m + 1
        # is odd, m is even, and we can factor x^n as x^n = x * x^m = x
        # * (x^2)^(m/2). If n is even then we can do x^n = (x^2)^(n/2)
        # as before.
        #
        # Here is the idea we'll use here. We can express
        # x^n = x^a + x^b where a is the largest power of 2 such that
        # n = a + b. To use this factorization in a clever way that lets
        # us achieve x^n in O(log(n)) multiplications, we keep the
        # provisional results of x^n in a variable called result and
        # iterate in the following way: for each iteration, if n is odd,
        # we multiply the result by x (if n is even, we do not), then we
        # set
        #
        # x -> x^2
        # n -> n // 2
        #
        # We continue until n == 1, at which point result = x^b, and
        # then multiply result by x^a to achieve x^n. n then becomes 0,
        # and we stop iterating.
        result = 1

        while n:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result


# @leet end
