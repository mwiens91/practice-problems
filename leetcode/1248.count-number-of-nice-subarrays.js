// @leet start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function (nums, k) {
  const counts = [1];
  let result = 0;
  let oddCount = 0;

  for (const num of nums) {
    if (num % 2 === 1) {
      oddCount++;
      counts.push(1);
    } else {
      counts[counts.length - 1]++;
    }

    if (oddCount >= k) {
      result += counts[oddCount - k];
    }
  }

  return result;
};
// @leet end
