// @leet start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  const res = [];

  const helper = (i) => {
    if (i == nums.length) {
      res.push([...nums]);
    }

    for (let j = i; j < nums.length; j++) {
      [nums[i], nums[j]] = [nums[j], nums[i]];

      helper(i + 1);

      [nums[i], nums[j]] = [nums[j], nums[i]];
    }
  };

  helper(0);

  return res;
};
// @leet end
