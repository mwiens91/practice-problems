# @leet start
class Solution:
    def numTrees(self, n: int) -> int:
        # We can do a bottom up dynamic programming solution. For any
        # given set of unique numbers {n_1, n_2, ..., n_m} we can choose
        # any number n_k as the root of a binary search tree. Suppose
        # there are N_smaller numbers smaller than n_k and N_larger
        # numbers larger than n_k. We need to find how many unique BSTs
        # there are for a tree with subtrees of N_smaller nodes on the
        # left and N_larger nodes on the right. This breaks down into
        # smaller problems of finding how many subtrees are possible
        # until we get to base case subtrees with no nodes or single
        # nodes.
        memo = {0: 1, 1: 1}

        for num_nodes in range(2, n + 1):
            num_trees_possible = 0

            for num_left_nodes in range(num_nodes):
                num_right_nodes = num_nodes - 1 - num_left_nodes
                num_trees_possible += memo[num_left_nodes] * memo[num_right_nodes]

            memo[num_nodes] = num_trees_possible

        return memo[n]


# @leet end
