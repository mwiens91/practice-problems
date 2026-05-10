# @leet start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        CODE_POINT_A = ord("a")

        n = len(s)
        counts = [0, 0, 0]
        right = 0  # exclusive

        def valid() -> bool:
            return counts[0] > 0 and counts[1] > 0 and counts[2] > 0

        def expand() -> bool:
            nonlocal right

            while right < n and not valid():
                counts[ord(s[right]) - CODE_POINT_A] += 1
                right += 1

            return valid()

        if not expand():
            return 0

        res = n - right + 1

        for ch in s:
            counts[ord(ch) - CODE_POINT_A] -= 1

            if not expand():
                return res

            res += n - right + 1

        return res


# @leet end
