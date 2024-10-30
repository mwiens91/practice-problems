# @leet start
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # For each string, group them together if their sorted strings
        # are equal. group_dict has a sorted string as a key and a list
        # of strings that much that counter as a value.
        group_dict = {}

        for str_ in strs:
            if (sorted_str := ''.join(sorted(str_))) in group_dict:
                group_dict[sorted_str].append(str_)
            else:
                group_dict[sorted_str] = [str_]

        return list(group_dict.values())
# @leet end
