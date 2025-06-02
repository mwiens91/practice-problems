# @leet start
import math


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # NOTE: I needed ChatGPT to understand the combinatorics for
        # this problem, but I'm going to explain how this works (in my
        # own words) below:
        #
        # For the unbounded case (no limit), this is the "stars and
        # bars" problem; we need to find the number of k-triplets
        # (x_1, x_2, ..., x_k)
        #
        # where
        #
        # x_1 + x_2 + ... + x_k = n,
        # x_i >= 0
        #
        # The solution to this problem is
        #
        # n + k - 1 \choose k - 1,
        #
        # where k = 3 in the case of this problem. However we have a
        # limit L that each child can receive. Let A be the set of all
        # 3-triplets corresponding to distributing n candies into
        # 3 bins, and let A_i represent the subset of all 3-triplets
        # where bin i has > L candies. Then our solution is given by
        #
        # |A| - |A_1 \union A_2 \union A_3|
        # = |A|
        # - |A_1| - |A_2| - |A_3|
        # + |A_1 \intersect A_2| + |A_1 \intersect A_3| + |A_2 \intersect A_3|
        # - |A_1 \intersect A_2 \intersect A_3|.
        #
        # Consider |A_1|. We want to find all triplets (x_1, x_2, x_3)
        # where
        #
        # x_1 + x_2 + x_3 = n,
        # x_1 > L,
        # x_2, x_3 >= 0.
        #
        # By doing a change of variables x_1' = x_1 - (L + 1) we have
        # x_1' >= 0 and
        #
        # x_1' + x_2 + x_3 = n - (L + 1),
        # x_1', x_2, x_3 >= 0.
        #
        # This has solution
        #
        # n - (L + 1) + k - 1 \choose k - 1,
        #
        # with k = 3.
        #
        # We can apply similar logic to come up with solutions to the
        # intersection size of 2 A_i and 3 A_is. Let m = 0, 1, 2, 3 be
        # the number of A_is being intersected (m = 0 corresponds to no
        # A_is being intersected, so just the regular solution to
        # |A|). Then the solution for each m is given by
        #
        # n - m * (L + 1) + k - 1 \choose k - 1,
        #
        # with k = 3 again.
        result = 0

        for m in range(4):
            sign = (-1) ** m
            num_intersections_with_size_m = math.comb(3, m)

            superset_size = n - m * (limit + 1) + 2

            if superset_size > 0:
                result += (
                    sign * num_intersections_with_size_m * math.comb(superset_size, 2)
                )
            else:
                break

        return result


# @leet end
