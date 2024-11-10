# @leet start
import random


class RandomizedSet:

    def __init__(self):
        # idx_dict has numbers we insert as keys and corresponding
        # indices as values. vals_list just stored our values and we get
        # their indices from the dictionary.
        self.idx_dict = dict()
        self.vals_list = []

    def insert(self, val: int) -> bool:
        if val in self.idx_dict:
            return False

        # Insert
        self.vals_list.append(val)
        self.idx_dict[val] = len(self.vals_list) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_dict:
            return False

        # Remove. To make this O(1) we'll swap val with the last thing
        # put in the list. First pop the last value off the list.
        last_val = self.vals_list.pop()

        # Put the last value (provided it is not the value we are
        # removing) where the value where we are removing lives
        if last_val != val:
            val_idx = self.idx_dict[val]
            self.vals_list[val_idx] = last_val
            self.idx_dict[last_val] = val_idx

        # Remove the value we need to remove from the index dictionary
        del self.idx_dict[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals_list)


# @leet end
