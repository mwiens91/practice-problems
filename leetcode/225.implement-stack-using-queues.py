# @leet start
from collections import deque

# NOTE: I'm using a deque here but I'll restrict it to using queue
# operations: so appendleft, pop, and [-1] indexing (peeking)


class MyStack:
    def __init__(self):
        self.queue = deque()

        # Assume this is never called on an empty stack, so we can
        # initialize this to anything here
        self.top_of_stack = 0

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

        self.top_of_stack = x

    def pop(self) -> int:
        # This has to be an O(n) operation unfortunately. Suppose the
        # queue as n elements. Then we rotate n - 2 of those elements to
        # the back. We record the next (n - 1)th element as the new top
        # of the stack and then rotate that one as well. Then we return
        # the nth element without putting it back in the stack. If
        # n == 1, we just do a normal pop.
        n = len(self.queue)

        if n == 1:
            return self.queue.pop()

        # Rotate n - 2 elements
        for _ in range(n - 2):
            self.queue.appendleft(self.queue.pop())

        # Record the (n - 1)th element as the top of the stack, then
        # rotate it
        self.top_of_stack = self.queue.pop()
        self.queue.appendleft(self.top_of_stack)

        # Pop and return the nth element
        return self.queue.pop()

    def top(self) -> int:
        return self.top_of_stack

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @leet end
