interface Array<T> {
  last(): T | -1;
}

Array.prototype.last = function <T>(this: T[]) {
  return this.length > 0 ? this[this.length - 1] : -1;
};
