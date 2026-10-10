// @leet start
/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function (nums, threshold) {
  const isValid = (divisor) =>
    nums.reduce((acc, curr) => acc + Math.ceil(curr / divisor), 0) <= threshold;

  let left = 1;
  let right = Math.max(...nums);

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (isValid(mid)) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
};
// @leet end
