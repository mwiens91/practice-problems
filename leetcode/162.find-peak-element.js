// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  // Check left and right
  if (nums.length === 1 || nums[0] > nums[1]) {
    return 0;
  }

  if (nums[nums.length - 1] > nums[nums.length - 2]) {
    return nums.length - 1;
  }

  let left = 0;
  let right = nums.length - 1;

  while (true) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) {
      return mid;
    }

    if (nums[mid - 1] > nums[mid]) {
      right = mid;
    } else {
      left = mid;
    }
  }
};
// @leet end
