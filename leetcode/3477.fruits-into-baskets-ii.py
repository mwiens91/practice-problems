# @leet start
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        num_types_unplaced = 0

        for num_fruits in fruits:
            # Place fruit into the first available basket
            for i, capacity in enumerate(baskets):
                if capacity >= num_fruits:
                    baskets[i] = 0

                    break
            else:
                # If no baskets are available, increment the number of
                # unplaced fruit types
                num_types_unplaced += 1

        return num_types_unplaced


# @leet end
