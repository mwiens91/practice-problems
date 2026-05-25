// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var limitOccurrences = function (nums, k) {
  const res = [];
  const counts = new Map();

  for (const num of nums) {
    counts.set(num, 1 + (counts.get(num) ?? 0));

    if (counts.get(num) <= k) {
      res.push(num);
    }
  }

  return res;
};
// @leet end
