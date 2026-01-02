// @leet start
class MyQueue {
  private readonly in: number[] = [];
  private readonly out: number[] = [];

  private cycleIfNeeded(): void {
    if (!this.out.length) {
      while (this.in.length) {
        this.out.push(this.in.pop()!);
      }
    }
  }

  push(x: number): void {
    this.in.push(x);
  }

  pop(): number {
    this.cycleIfNeeded();

    return this.out.pop()!;
  }

  peek(): number {
    this.cycleIfNeeded();

    return this.out[this.out.length - 1];
  }

  empty(): boolean {
    return !this.in.length && !this.out.length;
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
// @leet end
