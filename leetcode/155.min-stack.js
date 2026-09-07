// @leet start

var MinStack = function () {
  this.stack = [];
  this.monoStack = []; // monotonically nonincreasing
};

/**
 * @param {number} value
 * @return {void}
 */
MinStack.prototype.push = function (value) {
  this.stack.push(value);

  if (
    !this.monoStack.length ||
    value <= this.monoStack[this.monoStack.length - 1]
  ) {
    this.monoStack.push(value);
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  const val = this.stack.pop();

  if (val === this.monoStack[this.monoStack.length - 1]) {
    this.monoStack.pop();
  }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  return this.monoStack[this.monoStack.length - 1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @leet end
