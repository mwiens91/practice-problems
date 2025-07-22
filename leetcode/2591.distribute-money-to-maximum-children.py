# @leet start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            # Can't distribute at least $1 to all children
            return -1

        # Distribute $1 to everyone
        money -= children

        # Determine the maximum number of people we can distribute
        # exactly $7 more to while ensuring no one receives exactly $3
        # more
        groups = money // 7
        remainder = money % 7

        # Distribute $7 to each child
        if groups == children and remainder == 0:
            return groups

        # Distribute $7 to all but one child who recieves more than $7
        if groups >= children:
            return children - 1

        # Distribute $7 to groups number of children. There are at least
        # 2 children not receiving $7: they can divide the money so that
        # no one receives $3
        if children - groups > 1:
            return groups

        # We can give $7 to all but one child. If that child would
        # receive $3, give $7 to all but two children and have them
        # split the rest so that no one recieves $3; otherwise give $7
        # to all but one child.
        if remainder == 3:
            return groups - 1

        return groups


# @leet end
