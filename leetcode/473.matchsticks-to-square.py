# @leet start
class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        # Get out early if this isn't possible
        total_length = sum(matchsticks)

        if total_length % 4 != 0:
            return False

        # Get side length for the square
        required_side_length = total_length // 4

        # Define a recursive function to partition the matchsticks into
        # 4 sides which sum to required_side_length
        num_matchsticks = len(matchsticks)

        side_lengths = [0] * 4

        def is_square_possible(matchstick_idx: int = 0) -> bool:
            # If we've successfully iterated over all matchsticks, we've
            # made a square
            if matchstick_idx == num_matchsticks:
                return True

            # Try putting the matchstick on each side with a unique side
            # length
            side_lengths_seen = set()

            for side_length_idx, side_length in enumerate(side_lengths):
                # Skip this side if we've already done a side with the
                # same side length
                if side_length in side_lengths_seen:
                    continue

                side_lengths_seen.add(side_length)

                # Try putting the matchstick on the current side. If it
                # didn't work, reset the side and move to the next side.
                new_side_length = side_length + matchsticks[matchstick_idx]

                if new_side_length <= required_side_length:
                    side_lengths[side_length_idx] = new_side_length

                    if is_square_possible(matchstick_idx + 1):
                        return True

                    side_lengths[side_length_idx] = side_length

            # The matchstick can't result in a square with this
            # configuration
            return False

        return is_square_possible()


# @leet end
