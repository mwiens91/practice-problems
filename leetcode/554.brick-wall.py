# @leet start
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        # Get the number of edges (empty space that connects two bricks
        # horizonatally) we have for each x coordinate
        num_edges_per_x_coord_dict: dict[int, int] = {}

        for row in wall:
            x = 0

            for width in row[:-1]:
                x += width

                try:
                    num_edges_per_x_coord_dict[x] += 1
                except KeyError:
                    num_edges_per_x_coord_dict[x] = 1

        # The minimum number of crossed bricks is equal to the number or
        # rows minus the maximum number of edges that can occur at some
        # x-coordinate
        try:
            max_edges = max(num_edges_per_x_coord_dict.values())
        except ValueError:
            # No edges on any accessible x-coordinates
            max_edges = 0

        return len(wall) - max_edges


# @leet end
