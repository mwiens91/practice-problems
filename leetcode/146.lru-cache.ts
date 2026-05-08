// @leet start
class MyNode {
  constructor(
    public key: number,
    public val: number,
    public prev: MyNode | null = null,
    public next: MyNode | null = null,
  ) {}
}

class LRUCache {
  private size = 0;
  private capacity: number;
  private keyToNode = new Map<number, MyNode>();
  private head = new MyNode(-1, -1); // sentinel
  private tail = this.head;

  constructor(capacity: number) {
    this.capacity = capacity;
  }

  private moveToTail(nd: MyNode) {
    if (nd === this.tail) {
      return;
    }

    nd.prev!.next = nd.next;
    nd.next!.prev = nd.prev;

    nd.next = null;
    nd.prev = this.tail;
    this.tail.next = nd;
    this.tail = this.tail.next;
  }

  private addToTail(key: number, value: number) {
    this.tail.next = new MyNode(key, value, this.tail);
    this.tail = this.tail.next;

    this.keyToNode.set(key, this.tail);
  }

  // Precondition: size >= 1
  private removeOldest() {
    const toDelete = this.head.next!;
    this.head.next = toDelete.next;

    if (this.size === 1) {
      this.tail = this.head;
    } else {
      toDelete.next!.prev = this.head;
    }

    this.keyToNode.delete(toDelete.key);
    this.size--;
  }

  get(key: number): number {
    const target = this.keyToNode.get(key);

    if (!target) {
      return -1;
    }

    this.moveToTail(target);
    return target.val;
  }

  put(key: number, value: number) {
    const target = this.keyToNode.get(key);

    if (target != null) {
      target.val = value;
      this.moveToTail(target);
    } else {
      if (this.size == this.capacity) {
        this.removeOldest();
      }

      this.size++;
      this.addToTail(key, value);
    }
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @leet end
