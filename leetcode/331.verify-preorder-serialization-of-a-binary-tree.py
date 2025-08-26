# @leet start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        open_edges = 1

        for i, node in enumerate(nodes):
            if node == "#":
                open_edges -= 1

                # The number of open edges must never be negative and
                # can only (and must) be zero at the final node
                if open_edges < 0 or open_edges == 0 and i < len(nodes) - 1:
                    return False
            else:
                open_edges += 1

        return open_edges == 0


# @leet end
