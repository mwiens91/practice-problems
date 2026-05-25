// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSwaps = function (nums) {
  let left = 0;
  let right = nums.length - 1;
  let res = 0;

  while (left < right) {
    if (nums[right] === 0) {
      right--;
    } else {
      if (nums[left] === 0) {
        right--;
        res++;
      }

      left++;
    }
  }

  return res;
};
// @leet end
