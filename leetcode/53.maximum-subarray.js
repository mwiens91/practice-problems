// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let curr = 0;
  let min = 0;

  let res = nums[0];

  for (const num of nums) {
    curr += num;
    res = Math.max(res, curr - min);
    min = Math.min(min, curr);
  }

  return res;
};
// @leet end
