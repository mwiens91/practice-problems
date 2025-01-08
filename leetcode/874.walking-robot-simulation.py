# @leet start
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Put obstacles into a set
        obstacles_set: set[tuple[int, int]] = set()

        for obstacle_x, obstacle_y in obstacles:
            obstacles_set.add((obstacle_x, obstacle_y))

        # Robot position and orientation
        robot_position = [0, 0]

        UP = 0
        RIGHT = 1
        # DOWN = 2
        LEFT = 3

        orientation = UP

        # Follow each command and keep track of the max distance
        COMMAND_TURN_RIGHT = -1
        COMMAND_TURN_LEFT = -2

        max_distance = 0

        for command in commands:
            if command == COMMAND_TURN_RIGHT:
                orientation = (orientation + 1) % 4
            elif command == COMMAND_TURN_LEFT:
                orientation = (orientation - 1) % 4
            else:
                # Movement command
                num_steps = command

                # Find final position
                for _ in range(num_steps):
                    new_position = robot_position.copy()

                    if orientation == RIGHT:
                        new_position[0] += 1
                    elif orientation == LEFT:
                        new_position[0] -= 1
                    elif orientation == UP:
                        new_position[1] += 1
                    else:
                        # orientation == DOWN
                        new_position[1] -= 1

                    if tuple(new_position) in obstacles_set:
                        # Hit an obstacle, get out
                        break

                    robot_position = new_position

                max_distance = max(
                    max_distance, robot_position[0] ** 2 + robot_position[1] ** 2
                )

        return max_distance


# @leet end
