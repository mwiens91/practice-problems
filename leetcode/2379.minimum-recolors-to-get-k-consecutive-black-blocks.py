# @leet start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Use a sliding window to find the k-length window witht he
        # minimum number of "W"s
        current_num = blocks[:k].count("W")
        min_num = current_num

        for i in range(k, len(blocks)):
            current_num += (1 if blocks[i] == "W" else 0) + (
                -1 if blocks[i - k] == "W" else 0
            )

            min_num = min(min_num, current_num)

        return min_num


# @leet end
