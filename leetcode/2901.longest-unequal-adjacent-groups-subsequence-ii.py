# @leet start
class Solution:
    def getWordsInLongestSubsequence(
        self, words: list[str], groups: list[int]
    ) -> list[str]:
        def get_hamming_distance(s1: str, s2: str) -> int:
            # s1 and s2 must have equal lengths
            return sum(int(c1 != c2) for c1, c2 in zip(s1, s2))

        word_lengths = list(map(len, words))

        # Find the best subsequence length for subsequences ending at a
        # given word
        n = len(words)

        best_subseq_lengths = [1] * n
        prev_idx_used: list[int | None] = [None] * n

        for i in range(1, n):
            for j in range(i):
                if (
                    groups[i] != groups[j]
                    and word_lengths[i] == word_lengths[j]
                    and get_hamming_distance(words[i], words[j]) == 1
                    and (new_best_length := best_subseq_lengths[j] + 1)
                    > best_subseq_lengths[i]
                ):
                    # Update best subsequence length and previous index
                    # used
                    best_subseq_lengths[i] = new_best_length
                    prev_idx_used[i] = j

        # Get a maximal length subsequence by getting each word in
        # reverse order
        best_subseq_reversed: list[str] = []
        current_idx: int | None = best_subseq_lengths.index(max(best_subseq_lengths))

        while current_idx is not None:
            best_subseq_reversed.append(words[current_idx])
            current_idx = prev_idx_used[current_idx]

        return best_subseq_reversed[::-1]


# @leet end
