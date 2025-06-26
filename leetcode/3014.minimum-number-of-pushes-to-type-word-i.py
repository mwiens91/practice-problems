# @leet start
class Solution:
    def minimumPushes(self, word: str) -> int:
        total_pushes = 0

        # Assign letters the cheapest cost possible. We can have
        # - 8 letters with a push cost of 1
        # - 8 letters with a push cost of 2
        # - 8 letters with a push cost of 3
        # - 2 letters with a push cost of 4
        remaining_letters = len(word)
        current_push_cost = 1

        while remaining_letters > 0:
            letters_consumed = min(remaining_letters, 8)

            total_pushes += letters_consumed * current_push_cost
            remaining_letters -= letters_consumed

            current_push_cost += 1

        return total_pushes


# @leet end
