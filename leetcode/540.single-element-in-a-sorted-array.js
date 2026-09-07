// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (
      (mid % 2 === 0 &&
        mid !== nums.length - 1 &&
        nums[mid] === nums[mid + 1]) ||
      (mid % 2 === 1 && nums[mid] === nums[mid - 1])
    ) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return nums[left];
};
// @leet end
