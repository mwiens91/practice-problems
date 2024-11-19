# @leet start
class MyQueue:

    def __init__(self):
        # We have two stacks. We push to not_ready_to_pop stack. Once we
        # need to peek or pop, we transfer elements from the
        # not_ready_to_pop to the ready_to_pop stack, but in reverse
        # order so they're ready to pop (hence the name).
        self.not_ready_to_pop = []
        self.ready_to_pop = []

    def make_ready_to_pop(self) -> None:
        if self.ready_to_pop:
            return

        while self.not_ready_to_pop:
            self.ready_to_pop.append(self.not_ready_to_pop.pop())

    def push(self, x: int) -> None:
        self.not_ready_to_pop.append(x)

    def pop(self) -> int:
        if not self.ready_to_pop:
            self.make_ready_to_pop()

        return self.ready_to_pop.pop()

    def peek(self) -> int:
        if not self.ready_to_pop:
            self.make_ready_to_pop()

        return self.ready_to_pop[-1]

    def empty(self) -> bool:
        if not self.not_ready_to_pop and not self.ready_to_pop:
            # Both stacks empty
            return True

        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @leet end
