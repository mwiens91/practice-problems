# @leet start
class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        # Define the prefix and suffix function
        def is_prefix_and_suffix(str1: str, str2: str) -> bool:
            if str2.startswith(str1) and str2.endswith(str1):
                return True

            return False

        # Count the number of index pairs
        n = len(words)

        num_index_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                num_index_pairs += int(is_prefix_and_suffix(words[i], words[j]))

        return 0


# @leet end
