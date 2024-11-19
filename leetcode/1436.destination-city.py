# @leet start
class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        # Find city that is a destination but not a source
        sources = set()
        destinations = set()

        for source, destination in paths:
            sources.add(source)
            destinations.add(destination)

        for destination in destinations:
            if destination not in sources:
                return destination


# @leet end
