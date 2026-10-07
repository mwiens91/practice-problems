// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function (nums) {
  let curr = nums[0];
  let count = 1;
  let ascending = null; // null for not set; else boolean

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === curr) {
      continue;
    }

    if (ascending === null) {
      ascending = nums[i] > curr;
    }

    if ((ascending && nums[i] > curr) || (!ascending && nums[i] < curr)) {
      ascending = !ascending;
      count++;
    }

    curr = nums[i];
  }

  return count;
};
// @leet end
