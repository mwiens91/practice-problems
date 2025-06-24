# @leet start
from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}

        # This function counts the number of valid vowel substrings
        # (substrings containing all 5 vowels) in a substring of word
        # containing only vowels. The start index is inclusive and the
        # end index is exclusive.
        def count_vowel_substrings_in_vowel_run(start_idx: int, end_idx: int) -> int:
            valid_substring_count = 0

            # For each start index, use two pointers to find minimal
            # windows from each start index that contain all 5 vowels
            vowel_counts: defaultdict[str, int] = defaultdict(int)

            # The left index is inclusive and the right is exclusive
            left = start_idx
            right = start_idx

            while left < end_idx - 4 and right <= end_idx:
                # Get a minimal window from right that contains 5 vowels
                while right < end_idx and len(vowel_counts) < 5:
                    vowel_counts[word[right]] += 1
                    right += 1

                # Add substrings we can form using this window
                if len(vowel_counts) == 5:
                    valid_substring_count += end_idx - right + 1

                # Move the left pointer and reduce the count of the
                # vowel it pointed to
                vowel_counts[word[left]] -= 1

                if vowel_counts[word[left]] == 0:
                    del vowel_counts[word[left]]

                left += 1

            return valid_substring_count

        # Find maximal substrings containing vowels, and count the
        # number of valid vowel substrings that can be formed from it
        count = 0

        n = len(word)
        i = 0

        while i < n:
            # word[i] may or may not be a vowel
            start = i

            while i < n and word[i] in VOWELS:
                # word[i] is a vowel
                i += 1

            # i == n or word[i] is not a vowel
            if start < i:
                count += count_vowel_substrings_in_vowel_run(start, i)

            i += 1

        return count


# @leet end
