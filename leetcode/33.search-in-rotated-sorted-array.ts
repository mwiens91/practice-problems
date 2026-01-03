// @leet start
function search(nums: number[], target: number): number {
  // Find index of smallest num; it will be in lo
  let lo = 0;
  let hi = nums.length - 1;

  while (nums[lo] > nums[hi]) {
    const mid = Math.floor((lo + hi) / 2);

    if (nums[mid] > nums[hi]) {
      lo = mid + 1;
    } else {
      hi = mid;
    }
  }

  // Binary search for target
  if (target > nums[nums.length - 1]) {
    hi = lo - 1;
    lo = 0;
  } else {
    hi = nums.length - 1;
  }

  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    if (nums[mid] > target) {
      hi = mid - 1;
    } else {
      lo = mid + 1;
    }
  }

  return -1;
}
// @leet end
