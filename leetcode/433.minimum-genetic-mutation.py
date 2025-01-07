# @leet start
from collections import deque
import itertools


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # For some reason the start gene isn't always in the bank, so
        # add it now
        bank.append(startGene)

        # This can be interpreted as a graph problem. We'll say that two
        # genes have an edge between them if there is one mutation that
        # can turn one gene into another.
        def has_edge(gene1: str, gene2: str) -> bool:
            has_one_difference = False

            for base1, base2 in zip(gene1, gene2):
                if base1 != base2:
                    if has_one_difference:
                        # Found at least two differences, so no edge
                        return False

                    has_one_difference = True

            return True

        # Build edges dictionary
        edges: dictionary[str, list[str]] = {}

        for gene1, gene2 in itertools.combinations(bank, 2):
            if has_edge(gene1, gene2):
                # Add edge to dictionary
                for parent, child in [(gene1, gene2), (gene2, gene1)]:
                    try:
                        edges[parent].append(child)
                    except KeyError:
                        edges[parent] = [child]

        # Get out now if the starting gene has no edges
        if startGene not in edges:
            return -1

        # Do a breath-first search starting at the starting gene, and
        # return once and if we reach the ending gene. We'll enqueue
        # two-tuples containing the gene and its distance from the
        # starting gene.
        queue = deque([(startGene, 0)])
        visited = set()

        while queue:
            current_gene, distance = queue.pop()

            # If this is the end gene, return now
            if current_gene == endGene:
                return distance

            # Mark current gene as visited
            visited.add(current_gene)

            # Enqueue unvisited adjacent genes
            for adjacent_gene in edges[current_gene]:
                if adjacent_gene not in visited:
                    queue.appendleft((adjacent_gene, distance + 1))

        # Could not reach end gene
        return -1


# @leet end
