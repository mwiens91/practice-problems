# @leet start
class Solution:
    def isFascinating(self, n: int) -> bool:
        # NOTE: the below code is how you can find what the fascinating
        # numbers. Turns out there are just 4 of them.
        #
        # from itertools import chain
        # if 100 < n < 333:
        #     digits_set = set(chain.from_iterable([str(n), str(2 * n), str(3 * n)]))
        #
        #     if "0" not in digits_set and len(digits_set) == 9:
        #         return True
        #
        # return False
        return n in {192, 219, 273, 327}


# @leet end
