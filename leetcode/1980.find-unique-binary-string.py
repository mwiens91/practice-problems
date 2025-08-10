# @leet start
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # NOTE: Briefly glanced at the editorial to see if they thought
        # of something better than the solution I first thought of,
        # which is basically
        # - put nums in a set
        # - from 0 to infinity, choose the first number whose n-bit
        # representation does not appear in the nums set
        # The editorial had a super cool "diagonal argument" solution
        # which is used in set theory to prove that the real numbers are
        # uncountable. Too good not to use here. I feel honoured to be
        # typing something so cool.

        # There are n strings of length n. A string not present in these
        # n strings can be constructed by setting each ith bit to be
        # the reverse of the ith bit of the ith string.
        return "".join("1" if num[i] == "0" else "0" for i, num in enumerate(nums))


# @leet end
