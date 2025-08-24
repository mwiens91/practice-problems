# @leet start
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # From the examples I believe we are restricting
        # ourselves to positive integers, so
        #
        # sumOdd = sum(2k + 1, k=0...n-1) = n^2
        # sumEven = sum(2k, k=1...n) = n(n - 1)
        #
        # We can see that their GCD is n.
        return n


# @leet end
