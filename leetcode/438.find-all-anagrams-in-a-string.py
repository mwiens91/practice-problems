# @leet start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        CODE_POINT_A = ord("a")
        counts = [0] * 26
        nonzero_counts = 0

        def update(ch: str, delta: int) -> None:
            nonlocal nonzero_counts

            idx = ord(ch) - CODE_POINT_A

            # Simplifying assumption: delta != 0
            if counts[idx] == 0:
                nonzero_counts += 1
            elif counts[idx] + delta == 0:
                nonzero_counts -= 1

            counts[idx] += delta

        # Increment needed counts from p
        for ch in p:
            update(ch, 1)

        # Decrement needed counts from s[:len(p)]
        for i in range(len(p)):
            update(s[i], -1)

        # Is anagram at start index?
        res: list[int] = []

        for i in range(len(s) - len(p)):
            if nonzero_counts == 0:
                res.append(i)

            update(s[i], 1)
            update(s[i + len(p)], -1)

        if nonzero_counts == 0:
            res.append(len(s) - len(p))

        return res


# @leet end
