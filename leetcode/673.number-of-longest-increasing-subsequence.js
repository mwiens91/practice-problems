// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function (nums) {
  const maxLens = Array(nums.length).fill(1);
  const numWithMaxs = Array(nums.length).fill(1);

  let bestLen = 1;
  let numWithBest = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        if (maxLens[j] >= maxLens[i]) {
          maxLens[i] = maxLens[j] + 1;
          numWithMaxs[i] = numWithMaxs[j];
        } else if (maxLens[j] === maxLens[i] - 1) {
          numWithMaxs[i] += numWithMaxs[j];
        }
      }
    }

    if (maxLens[i] > bestLen) {
      bestLen = maxLens[i];
      numWithBest = numWithMaxs[i];
    } else if (maxLens[i] === bestLen) {
      numWithBest += numWithMaxs[i];
    }
  }

  return numWithBest;
};
// @leet end
