// @leet start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function (nums, target) {
  const totalSum = nums.reduce((acc, x) => acc + x);

  if (Math.abs(target) > totalSum) {
    return 0;
  }

  let prevCounts = Array(2 * totalSum + 1).fill(0);
  prevCounts[totalSum] = 1;

  for (const num of nums) {
    const currCounts = Array(2 * totalSum + 1).fill(0);

    for (
      let partialSum = -totalSum + num;
      partialSum <= totalSum - num;
      partialSum++
    ) {
      currCounts[partialSum - num + totalSum] +=
        prevCounts[partialSum + totalSum];
      currCounts[partialSum + num + totalSum] +=
        prevCounts[partialSum + totalSum];
    }

    prevCounts = currCounts;
  }

  return prevCounts[target + totalSum];
};
// @leet end
