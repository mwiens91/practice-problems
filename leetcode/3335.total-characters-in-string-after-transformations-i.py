# @leet start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ANSWER_MODULUS = int(1e9 + 7)

        # Create frequency list
        freqs = [0] * 26

        for char in s:
            freqs[ord(char) - ord('a')] += 1

        # Do 26 transformations at a time until we're under 26
        # transformations
        while t >= 26:
            new_freqs = [0] * 26

            # A - Y
            for i in range(25):
                new_freqs[i] += freqs[i]
                new_freqs[i + 1] += freqs[i]

            # Z
            new_freqs[25] += freqs[25]
            new_freqs[0] += freqs[25]
            new_freqs[1] += freqs[25]

            t -= 26
            freqs = new_freqs

        # Return final length
        final_length = sum(freqs[0 : 26 - t]) + 2 * sum(freqs[26 - t :])

        return final_length % ANSWER_MODULUS


# @leet end
