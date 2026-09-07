// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  let prev = nums[0];
  let curr = Math.max(nums[0], nums[1] ?? 0);

  for (let i = 2; i < nums.length; i++) {
    [prev, curr] = [curr, Math.max(curr, prev + nums[i])];
  }

  return curr;
};
// @leet end
