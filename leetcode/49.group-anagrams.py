# @leet start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # For each string, group them together if their character counts
        # are equal. group_dict has a sorted string as a key and a list
        # of strings that much that counter as a value.
        group_dict = {}

        for str_ in strs:
            # TODO: If we let m indicate the maximum length of strings
            # given and n indicate the number of strings we're given,
            # then sorting here makes the time complexity O(nm logm).
            # We might be able to get this down to O(nm) if we find some
            # way to hash a counter of each string and use this as a
            # key. Probably not hard. Does need a bit of
            # thinking/Googling. Not going to bother doing this here.
            # Rather move on.
            if (sorted_str := "".join(sorted(str_))) in group_dict:
                group_dict[sorted_str].append(str_)
            else:
                group_dict[sorted_str] = [str_]

        return list(group_dict.values())


# @leet end
