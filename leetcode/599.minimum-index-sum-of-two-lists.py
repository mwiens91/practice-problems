# @leet start
import math


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Find the minimum indices for list1 and list2 at which words occur
        list1_word_idxs: dict[str, int] = {}
        list2_word_idxs: dict[str, int] = {}

        for word_list, word_idxs_dict in zip(
            [list1, list2], [list1_word_idxs, list2_word_idxs]
        ):
            for i, word in enumerate(word_list):
                if word not in word_idxs_dict:
                    word_idxs_dict[word] = i

        # Iterate over list1 words and find shared words with the least
        # index sum
        least_idx_sum = math.inf
        words_with_least_idx_sum: list[str] = []

        for word, list1_idx_sum in list1_word_idxs.items():
            if word not in list2_word_idxs:
                continue

            idx_sum = list1_idx_sum + list2_word_idxs[word]

            if idx_sum < least_idx_sum:
                least_idx_sum = idx_sum
                words_with_least_idx_sum = [word]
            elif idx_sum == least_idx_sum:
                words_with_least_idx_sum.append(word)

        return words_with_least_idx_sum


# @leet end
