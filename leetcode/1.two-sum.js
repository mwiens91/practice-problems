// @leet start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const seen = new Map();

  for (const [i, num] of nums.entries()) {
    if (seen.has(target - num)) {
      return [i, seen.get(target - num)];
    }

    seen.set(num, i);
  }
};
// @leet end
