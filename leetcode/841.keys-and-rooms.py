# @leet start
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set([0])
        to_visit = [0]

        while to_visit:
            room_idx = to_visit.pop()

            for adj_idx in rooms[room_idx]:
                if adj_idx not in visited:
                    visited.add(adj_idx)
                    to_visit.append(adj_idx)

        return len(visited) == len(rooms)


# @leet end
