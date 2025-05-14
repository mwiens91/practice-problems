# @leet start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        NORTH = "N"
        SOUTH = "S"
        EAST = "E"
        # WEST = "W"

        visited = set([(0, 0)])

        current_pos = [0, 0]

        for direction in path:
            if direction == NORTH:
                current_pos[1] += 1
            elif direction == SOUTH:
                current_pos[1] -= 1
            elif direction == EAST:
                current_pos[0] += 1
            else:
                # direction == WEST
                current_pos[0] -= 1

            position_tuple = tuple(current_pos)

            if position_tuple in visited:
                return True

            visited.add(position_tuple)

        return False


# @leet end
