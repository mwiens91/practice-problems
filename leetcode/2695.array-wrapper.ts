class ArrayWrapper {
  private nums: number[];
  private cachedSum: number | null = null;

  constructor(nums: number[]) {
    this.nums = nums;
  }

  valueOf(): number {
    if (this.cachedSum === null) {
      this.cachedSum = this.nums.reduce((accum, val) => accum + val, 0);
    }

    return this.cachedSum;
  }

  toString(): string {
    return "[" + this.nums.toString() + "]";
  }
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
