# @leet start
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)

        all_source_to_target_paths: list[list[int]] = []
        current_path: list[int] = []

        def find_paths_to_target(current_node: int = 0) -> None:
            # Add current node to path
            current_path.append(current_node)

            # If this is the final node, add this path to the source to
            # target paths. Otherwise recurse into adjacent nodes.
            if current_node == n - 1:
                all_source_to_target_paths.append(current_path.copy())
            else:
                for adjacent_node in graph[current_node]:
                    find_paths_to_target(adjacent_node)

            # Remove current node from path
            current_path.pop()

        find_paths_to_target()

        return all_source_to_target_paths


# @leet end
