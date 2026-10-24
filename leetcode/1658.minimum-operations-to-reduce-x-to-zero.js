// @leet start
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function (nums, x) {
  let best = Infinity;
  let outsideSum = nums.reduce((acc, curr) => acc + curr);

  if (outsideSum < x) {
    return -1;
  }

  let start = 0;

  for (let i = 0; i < nums.length; i++) {
    outsideSum -= nums[i];

    while (outsideSum < x) {
      outsideSum += nums[start];
      start++;
    }

    if (outsideSum === x) {
      best = Math.min(best, nums.length - i + start - 1);
    }
  }

  return best < Infinity ? best : -1;
};
// @leet end
