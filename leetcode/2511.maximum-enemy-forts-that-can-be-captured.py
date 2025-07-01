# @leet start
class Solution:
    def captureForts(self, forts: list[int]) -> int:
        ALLY_FORT = 1
        EMPTY_FORT = -1
        ENDPOINT_FORT_TYPES = {ALLY_FORT, EMPTY_FORT}

        # Endpoint forts are either ally forts or empty forts
        last_endpoint_fort_type: None | int = None

        max_distance = 0
        current_distance = 0

        for fort in forts:
            if fort in ENDPOINT_FORT_TYPES:
                # If the endpoints are opposite fort types, this is a
                # valid line
                if {fort, last_endpoint_fort_type} == ENDPOINT_FORT_TYPES:
                    max_distance = max(max_distance, current_distance)

                last_endpoint_fort_type = fort
                current_distance = 0
            else:
                current_distance += 1

        return max_distance


# @leet end
