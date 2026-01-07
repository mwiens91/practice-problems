// @leet start
class OrderedStream {
  private readonly vals: (string | null)[];
  private ptr = 0;

  constructor(n: number) {
    this.vals = new Array(n).fill(null);
  }

  insert(idKey: number, value: string): string[] {
    this.vals[idKey - 1] = value;
    const start = this.ptr;

    while (this.ptr < this.vals.length && this.vals[this.ptr] !== null) {
      this.ptr++;
    }

    return this.vals.slice(start, this.ptr) as string[];
  }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
// @leet end
