# @leet start
class ListNode:
    def __init__(
        self, val: int, prev: ListNode | None = None, next: ListNode | None = None
    ):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(-1)
        self.tail = self.dummy
        self.size = 0

    def _getNode(self, index: int) -> ListNode:
        if self.size - 1 <= 2 * index:
            # Backwards from tail
            curr = self.tail

            for _ in range(self.size - 1 - index):
                curr = curr.prev

            return curr

        # Forwards from head
        curr = self.dummy

        for _ in range(index + 1):
            curr = curr.next

        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        return self._getNode(index).val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val, self.tail)
        self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
        else:
            parent = self._getNode(index - 1)
            parent.next = ListNode(val, parent, parent.next)

            if parent.next.next:
                parent.next.next.prev = parent.next

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            to_delete = self._getNode(index)

            to_delete.prev.next = to_delete.next
            to_delete.next.prev = to_delete.prev

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @leet end
