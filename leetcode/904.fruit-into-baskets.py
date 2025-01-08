# @leet start
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # We'll keep a dictionary that has fruits as keys and indices at
        # which we last saw that fruit as values. We'll enforce the size
        # of the dictionary to be at most two in the code below.
        last_seen_dict: dict[int, int] = {}

        # Determine the maximum number of fruits we can pick
        maximum_run = 0
        current_run = 0
        start_idx = 0

        for i, fruit in enumerate(fruits):
            # Remove oldest fruit if this is a new type of fruit and we
            # already have two types in our basket
            if fruit not in last_seen_dict and len(last_seen_dict) >= 2:
                # Note that initializing the oldest fruit index to the
                # current fruit index is just a way to ensure that the
                # initial value is greater than any value in the
                # dictionary
                fruit_to_remove = None
                oldest_fruit_idx = i

                for seen_fruit, last_seen_idx in last_seen_dict.items():
                    if last_seen_idx < oldest_fruit_idx:
                        fruit_to_remove = seen_fruit
                        oldest_fruit_idx = last_seen_idx

                # Subtract from the current run and remove the fruit to
                # remove
                new_start_idx = oldest_fruit_idx + 1

                current_run -= new_start_idx - start_idx

                start_idx = new_start_idx
                del last_seen_dict[fruit_to_remove]

            # Update last seen dict and increment current run value
            last_seen_dict[fruit] = i
            current_run += 1

            # Update max
            maximum_run = max(maximum_run, current_run)

        return maximum_run


# @leet end
