# @leet start
class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        CODE_POINT_A = ord("a")
        keys: set[tuple[int, ...]] = set()

        for word in words:
            even_counts = [0] * 26
            odd_counts = [0] * 26

            for i, ch in enumerate(word):
                if i % 2 == 0:
                    even_counts[ord(ch) - CODE_POINT_A] += 1
                else:
                    odd_counts[ord(ch) - CODE_POINT_A] += 1

            keys.add(tuple(even_counts + odd_counts))

        return len(keys)


# @leet end
