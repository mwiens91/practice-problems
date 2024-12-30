# @leet start
class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        last_seen = [None] * 26

        def char_to_idx(char: str) -> int:
            return ord(char) - ord("a")

        for idx, char in enumerate(s):
            char_idx = char_to_idx(char)

            if (prev_idx := last_seen[char_idx]) is not None:
                # Seen char already
                if idx - prev_idx - 1 != distance[char_idx]:
                    return False
            else:
                # Haven't seen char
                last_seen[char_idx] = idx

        return True


# @leet end
