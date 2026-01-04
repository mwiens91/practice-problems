// @leet start
/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  let left = 0;
  let curr = 0;
  let right = nums.length - 1;

  while (curr <= right) {
    if (nums[curr] === 2) {
      [nums[curr], nums[right]] = [nums[right], nums[curr]];
      right--;
    } else if (nums[curr] === 0) {
      [nums[left], nums[curr]] = [nums[curr], nums[left]];
      left++;
      curr++;
    } else {
      curr++;
    }
  }
}
// @leet end
