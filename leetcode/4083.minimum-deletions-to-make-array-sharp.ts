// @leet start
function minDeletions(nums: number[]): number {
  let res = 0;
  let prev = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === prev) {
      res++;
    } else {
      prev = nums[i];
    }
  }

  return res;
}
// @leet end
