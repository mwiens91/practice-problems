# @leet start
class Solution:
    def minimumChairs(self, s: str) -> int:
        ENTER = "E"
        # LEAVE = "L"

        max_seats_needed = 0
        current_seats_needed = 0

        for event in s:
            if event == ENTER:
                current_seats_needed += 1
                max_seats_needed = max(max_seats_needed, current_seats_needed)
            else:
                current_seats_needed -= 1

        return max_seats_needed


# @leet end
