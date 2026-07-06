// @leet start
function isMiddleElementUnique(nums: number[]): boolean {
  const mid = (nums.length - 1) / 2;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[mid] && i !== mid) {
      return false;
    }
  }

  return true;
}
// @leet end
