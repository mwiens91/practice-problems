# @leet start
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        out_degree = [0] * n
        dest_to_sources: list[list[int]] = [[] for _ in range(n)]
        res: list[int] = []

        for src, edges in enumerate(graph):
            out_degree[src] = len(edges)

            if out_degree[src] == 0:
                res.append(src)

            for dest in edges:
                dest_to_sources[dest].append(src)

        i = 0

        while i < len(res):
            for src in dest_to_sources[res[i]]:
                out_degree[src] -= 1

                if out_degree[src] == 0:
                    res.append(src)

            i += 1

        return sorted(res)


# @leet end
