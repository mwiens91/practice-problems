# @leet start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Sort both arrays based on the descending order of position;
        # this will change the position and speed variables from lists
        # to tuples, but that does not matter here
        position, speed = zip(*sorted(zip(position, speed), reverse=True))

        # Idea: the first car will set the best possible finishing
        # time. The subsequent cars will either finish at the same time
        # (joining the fleet) or finish at a later time, setting a new
        # best possible finishing time and making a new fleet. We just
        # need to count the number of fleets that occur.

        # Process the car in index one (the one with the furthest
        # position) here first before iterating.
        num_fleets = 1
        best_possible_time = (target - position[0]) / speed[0]

        for this_position, this_speed in zip(position[1:], speed[1:]):
            finish_time = (target - this_position) / this_speed

            # If slower, new fleet
            if finish_time > best_possible_time:
                best_possible_time = finish_time
                num_fleets += 1

        return num_fleets
# @leet end
