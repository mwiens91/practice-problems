// @leet start
class MinStack {
  private readonly stack: number[] = [];
  private readonly minStack: number[] = [];

  push(val: number): void {
    this.stack.push(val);

    if (
      !this.minStack.length ||
      val <= this.minStack[this.minStack.length - 1]
    ) {
      this.minStack.push(val);
    }
  }

  pop(): void {
    const temp = this.stack.pop();

    if (this.minStack[this.minStack.length - 1] === temp) {
      this.minStack.pop();
    }
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.minStack[this.minStack.length - 1];
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @leet end
