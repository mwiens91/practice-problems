# @leet start
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # O(n log n) solution. Find the maximum distance from any house
        # to its closest heater. First sort, then do a binary search on
        # each house.
        houses.sort()
        heaters.sort()

        max_radius_required = 0
        num_heaters = len(heaters)

        for house_position in houses:
            left = 0
            right = num_heaters - 1

            smallest_heater_radius = abs(house_position - heaters[0])

            while left <= right:
                mid = (left + right) // 2
                heater_position = heaters[mid]

                # Update best heater
                smallest_heater_radius = min(
                    smallest_heater_radius, abs(house_position - heater_position)
                )

                # Get out or move pointers
                if heater_position == house_position:
                    break

                if heater_position < house_position:
                    left = mid + 1
                else:
                    # heater_position > house_position
                    right = mid - 1

            max_radius_required = max(max_radius_required, smallest_heater_radius)

        return max_radius_required


# @leet end
