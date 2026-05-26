// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let res = 0;
  let count = 0;

  let left = 0;
  let right = 0;

  while (right < nums.length) {
    while (right < nums.length && (count < k || nums[right] !== 0)) {
      if (nums[right] === 0) {
        count++;
      }

      right++;
    }

    res = Math.max(res, right - left);

    if (nums[left] === 0) {
      count--;
    }

    left++;
  }

  return res;
};
// @leet end
