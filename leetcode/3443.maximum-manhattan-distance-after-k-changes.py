# @leet start
import itertools


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # Find the best distance possible in an ordinal direction (NW,
        # NE, etc.) while making at most k changes. goes_up is True if
        # the direction includes N, else False. goes_right is True if
        # the direction includes E, else False.
        def best_distance_in_ordinal_direction(goes_up: bool, goes_right: bool) -> int:
            position_sum = 0
            best_distance = 0
            changes_remaining = k

            def process_move(in_target_dir: bool) -> None:
                nonlocal position_sum, best_distance, changes_remaining

                if in_target_dir:
                    position_sum += 1
                elif changes_remaining > 0:
                    position_sum += 1
                    changes_remaining -= 1
                else:
                    position_sum -= 1

                best_distance = max(best_distance, position_sum)

            for direction in s:
                match direction:
                    case "N":
                        process_move(goes_up)
                    case "E":
                        process_move(goes_right)
                    case "S":
                        process_move(not goes_up)
                    case _:
                        # "W"
                        process_move(not goes_right)

            return best_distance

        return max(
            best_distance_in_ordinal_direction(up, right)
            for up, right in itertools.product([True, False], repeat=2)
        )


# @leet end
