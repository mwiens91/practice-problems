# @leet start
from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Make graph of characters where an edge between two characters
        # mean they are equivalent
        edges: defaultdict[str, set[str]] = defaultdict(set)

        for char1, char2 in zip(s1, s2):
            edges[char1].add(char2)
            edges[char2].add(char1)

        # Find the smallest equivalent character for each component
        smallest_equivalent_dict: dict[str, str] = {}
        seen: set[str] = set()

        for char in edges:
            if char in seen:
                continue

            # Traverse the component
            component_chars = set([char])
            smallest_char = char
            to_visit = [char]

            while to_visit:
                this_char = to_visit.pop()

                for adj_char in edges[this_char]:
                    if adj_char in component_chars:
                        continue

                    component_chars.add(adj_char)
                    smallest_char = min(smallest_char, adj_char)
                    to_visit.append(adj_char)

            # Set smallest equivalent character and update seen set
            for this_char in component_chars:
                smallest_equivalent_dict[this_char] = smallest_char

            seen |= component_chars

        return "".join(smallest_equivalent_dict.get(char, char) for char in baseStr)


# @leet end
