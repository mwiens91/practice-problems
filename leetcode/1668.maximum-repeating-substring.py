# @leet start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        word_len = len(word)
        seq_len = len(sequence)

        # Store the number of repetitions of word that end at each index
        # i
        repetitions = [0] * seq_len
        best_repeats = 0

        for i in range(word_len - 1, seq_len):
            if sequence[i - word_len + 1 : i + 1] == word:
                repetitions[i] = 1

                if i >= word_len:
                    repetitions[i] += repetitions[i - word_len]

                best_repeats = max(best_repeats, repetitions[i])

        return best_repeats


# @leet end
