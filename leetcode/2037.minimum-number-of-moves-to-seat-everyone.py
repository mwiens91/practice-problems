# @leet start
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        # Sort seats and students
        seats.sort()
        students.sort()

        # Greedily position the ith furthest student in the ith seat
        moves = 0

        for seat, student in zip(seats, students):
            moves += abs(seat - student)

        return moves


# @leet end
