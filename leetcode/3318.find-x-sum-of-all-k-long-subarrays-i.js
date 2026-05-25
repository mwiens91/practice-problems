// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function (nums, k, x) {
  const counts = new Map();

  const getXSum = () =>
    [...counts.entries()]
      .sort((a, b) => b[1] - a[1] || b[0] - a[0])
      .slice(0, x)
      .reduce((acc, curr) => acc + curr[0] * curr[1], 0);

  const res = [];

  for (let i = 0; i < nums.length; i++) {
    counts.set(nums[i], 1 + (counts.get(nums[i]) ?? 0));

    if (i >= k - 1) {
      res.push(getXSum());
      counts.set(nums[i - k + 1], counts.get(nums[i - k + 1]) - 1);
    }
  }

  return res;
};
// @leet end
