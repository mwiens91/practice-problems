# @leet start
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t_idxs = {char: idx for idx, char in enumerate(t)}

        return sum(abs(s_idx - t_idxs[char]) for s_idx, char in enumerate(s))


# @leet end
