// @leet start
var RandomizedSet = function () {
  this.valToIdx = new Map();
  this.valArray = [];
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function (val) {
  if (this.valToIdx.has(val)) {
    return false;
  }

  this.valToIdx.set(val, this.valArray.length);
  this.valArray.push(val);

  return true;
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function (val) {
  if (!this.valToIdx.has(val)) {
    return false;
  }

  const removeValIdx = this.valToIdx.get(val);

  if (this.valArray.length > 1) {
    this.valToIdx.set(this.valArray[this.valArray.length - 1], removeValIdx);
    this.valArray[removeValIdx] = this.valArray[this.valArray.length - 1];
  }

  this.valToIdx.delete(val);
  this.valArray.pop();

  return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function () {
  return this.valArray[Math.floor(Math.random() * this.valArray.length)];
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
// @leet end
