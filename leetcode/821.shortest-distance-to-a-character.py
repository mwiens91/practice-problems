# @leet start
import math


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        # Find least distance to the character once its on the left.
        # Then find least distance to the character once its on the
        # right and take the minimum.
        n = len(s)

        distances = [math.inf] * n

        def find_left_or_right_distances(left: bool) -> None:
            # Find first occurance of the character from the left or
            # right
            i, i_delta = (0, 1) if left else (n - 1, -1)

            while s[i] != c:
                i += i_delta

            # Find left or right distances
            distance = 0

            remaining_range = range(i, n) if left else range(i, -1, -1)

            for j in remaining_range:
                print(j)
                # Reset distance if we hit the character; else increment
                if s[j] == c:
                    distance = 0
                else:
                    distance += 1

                distances[j] = min(distances[j], distance)

        find_left_or_right_distances(left=True)
        find_left_or_right_distances(left=False)

        return distances


# @leet end
