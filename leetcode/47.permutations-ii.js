// @leet start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function (nums) {
  const res = [];

  const helper = (i) => {
    if (i == nums.length) {
      res.push([...nums]);
    }

    const seen = new Set();

    for (let j = i; j < nums.length; j++) {
      if (seen.has(nums[j])) {
        continue;
      }

      seen.add(nums[j]);

      [nums[i], nums[j]] = [nums[j], nums[i]];
      helper(i + 1);
      [nums[i], nums[j]] = [nums[j], nums[i]];
    }
  };

  helper(0);

  return res;
};
// @leet end
