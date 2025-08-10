# @leet start
class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        # NOTE: Probably can do better than brute force. I just want to
        # do a problem fast while I wait for a friend.
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[j] - arr[i]) > a:
                    continue

                for k in range(j + 1, n):
                    if abs(arr[k] - arr[j]) <= b and abs(arr[k] - arr[i]) <= c:
                        count += 1

        return count


# @leet end
