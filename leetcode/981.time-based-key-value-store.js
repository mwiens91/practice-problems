// @leet start
var TimeMap = function () {
  this.map = new Map(); // Map<string, [int, string][]>
};

/**
 * @param {string} key
 * @param {string} value
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function (key, value, timestamp) {
  if (!this.map.has(key)) {
    this.map.set(key, []);
  }

  this.map.get(key).push([timestamp, value]);
};

/**
 * @param {string} key
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function (key, timestamp) {
  if (!this.map.has(key)) {
    return "";
  }

  const vals = this.map.get(key);

  if (vals[0][0] > timestamp) {
    return "";
  }

  let left = 0;
  let right = vals.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (vals[mid][0] <= timestamp) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return vals[right][1];
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
// @leet end
