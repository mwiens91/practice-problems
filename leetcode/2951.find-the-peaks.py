# @leet start
class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        peaks: list[int] = []

        i = 1

        while i < len(mountain) - 1:
            if mountain[i - 1] < mountain[i] and mountain[i + 1] < mountain[i]:
                peaks.append(i)

                # If we're at a peak, the next height cannot be a peak
                i += 2
            else:
                i += 1

        return peaks


# @leet end
