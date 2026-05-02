# @leet start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_lists: list[list[int]] = [[] for _ in range(numCourses)]
        in_degrees: list[int] = [0 for _ in range(numCourses)]

        for child, parent in prerequisites:
            adj_lists[parent].append(child)
            in_degrees[child] += 1

        stack = [node for node, deg in enumerate(in_degrees) if deg == 0]

        while stack:
            node = stack.pop()

            for adj_node in adj_lists[node]:
                in_degrees[adj_node] -= 1

                if in_degrees[adj_node] == 0:
                    stack.append(adj_node)

        return all(deg == 0 for deg in in_degrees)


# @leet end
