// @leet start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var maxNonOverlapping = function (nums, target) {
  let prefixSums = new Set([0]);
  let currSum = 0;
  let result = 0;

  for (const num of nums) {
    currSum += num;

    if (prefixSums.has(currSum - target)) {
      result++;

      prefixSums = new Set([0]);
      currSum = 0;
    } else {
      prefixSums.add(currSum);
    }
  }

  return result;
};
// @leet end
