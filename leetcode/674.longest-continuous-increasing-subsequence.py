# @leet start
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        # Idea, two pointers: a start pointer i and a moving pointer j.
        # We move until we hit a non-increasing element, then update the
        # best we've seen so far with the subsequence that just ended.
        n = len(nums)

        i = 0
        j = 0

        best = 1

        # We're going to compare with the element past j, so we need to
        # make sure it exists
        while j + 1 < n:
            if nums[j] < nums[j + 1]:
                j += 1
            else:
                # End of this subsequence. Update best and the pointers,
                # and continue with the next subsequence.
                best = max(best, j - i + 1)

                i = j + 1
                j = i

        # Calculate the last subsequence
        best = max(best, j - i + 1)

        return best


# @leet end
