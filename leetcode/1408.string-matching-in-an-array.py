# @leet start
from collections import defaultdict


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        # First partition words by their length
        words_of_length_dict: defaultdict[int, list[str]] = defaultdict(list)

        for word in words:
            words_of_length_dict[len(word)].append(word)

        # Now find all words which are substrings of other words by
        # testing all words of a given length with words of shorter
        # lengths
        lengths = sorted(words_of_length_dict.keys())

        possible_substrings = set(words_of_length_dict[lengths[0]])
        actual_substrings: set[str] = set()

        for length in lengths[1:]:
            words_to_test = words_of_length_dict[length]

            for word in words_to_test:
                matched_substrings: set[str] = set()

                for possible_substring in possible_substrings:
                    if possible_substring in word:
                        matched_substrings.add(possible_substring)

                possible_substrings.difference_update(matched_substrings)
                actual_substrings.update(matched_substrings)

            possible_substrings.update(words_to_test)

        return list(actual_substrings)


# @leet end
