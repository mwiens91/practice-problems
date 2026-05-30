// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const n = nums.length;

  return Math.floor((n * (n + 1)) / 2) - nums.reduce((acc, curr) => acc + curr);
};
// @leet end
