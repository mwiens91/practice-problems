# @leet start
class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        res = 0

        for i in range(n):
            xor = arr[i]

            for k in range(i + 1, n):
                xor ^= arr[k]

                if xor == 0:
                    res += k - i

        return res


# @leet end
