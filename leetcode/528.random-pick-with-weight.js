// @leet start
/**
 * @param {number[]} w
 */
var Solution = function (w) {
  for (let i = 1; i < w.length; i++) {
    w[i] += w[i - 1];
  }

  this.w = w.map((x) => x / w[w.length - 1]);
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function () {
  const r = Math.random();

  let left = 0;
  let right = this.w.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (this.w[mid] > r) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
// @leet end
