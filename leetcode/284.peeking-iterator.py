# @leet start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        # Store iterator
        self.iterator = iterator

        # Always have next element on hand
        self.next_element = None

        self.cycle_next_element()

    def cycle_next_element(self):
        """
        Cycles the next value of the iterator into the next variable.
        :rtype: None
        """
        if self.iterator.hasNext():
            self.next_element = self.iterator.next()
        else:
            self.next_element = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_element

    def next(self):
        """
        :rtype: int
        """
        # Get current next element
        current_next = self.next_element

        self.cycle_next_element()

        return current_next

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_element is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @leet end
