# @leet start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # We'll take all elements out of the nested list and put them
        # into a values list
        self.values: list[int] = []

        def recursive_to_get_values(nested_int: NestedInteger) -> None:
            if nested_int.isInteger():
                self.values.append(nested_int.getInteger())
            else:
                for child_nested_int in nested_int.getList():
                    recursive_to_get_values(child_nested_int)

        for nested_int in nestedList:
            recursive_to_get_values(nested_int)

        # Keep track of current index into the values list and total
        # size
        self.current_index = 0
        self.size = len(self.values)

    def next(self) -> int:
        value = self.values[self.current_index]

        self.current_index += 1

        return value

    def hasNext(self) -> bool:
        return self.current_index < self.size


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @leet end
